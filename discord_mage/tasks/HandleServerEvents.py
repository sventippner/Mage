from datetime import datetime

import discord
from discord.ext import tasks

from mage.models.Event import Event
from mage.models.Server import Server
from mage.models.User import User
from utils import data_access


class HandleServerEvents:

    def __init__(self, client):
        self.client = client

    @tasks.loop(minutes=15)
    async def call(self):
        now = datetime.now()
        all_events = data_access.find(Event)
        for event in all_events:
            if now >= event.end_date:
                await self.action_end_event(event)

    async def action_end_event(self, event: Event):
        max_points, gathered_points = self.action_get_points(event)
        winners = self.action_get_winners(max_points, event)
        self.action_reward_winners(event, winners)
        announce_string = await self.action_create_announcement_string(event, max_points, gathered_points)
        await self.action_announce_winner(announce_string, event)
        self.action_delete_document(event)

    def action_reward_winners(self, event: Event, winners):
        for winner_id in winners:
            user = data_access.find_one(User, discord_user_id=winner_id, discord_guild_id=event.discord_guild_id)
            if user:
                for reward in event.rewards:
                    user.obtain_item(reward)
                user.save()

    async def action_create_announcement_string(self, event, max_points, gathered_points):
        announce_string = f"{event.name} has ended!\n\n"
        guild = self.client.get_guild(id=event.discord_guild_id)
        server = data_access.find_one(Server, discord_guild_id=event.discord_guild_id)
        winner_list = []
        for role_id, points in gathered_points.items():
            role = discord.utils.get(guild.roles, id=role_id)
            announce_string += f"{role.mention} gathered **{points}** {server.points_name}.\n"
            if points == max_points and max_points != 0:
                winner_list.append(role)
        announce_string += "\nWinner:"
        if winner_list:
            for winner in winner_list:
                announce_string += f" {winner.mention}"
            announce_string += f"\nRewards: {event.rewards}"
        else:
            announce_string += " Nobody participated."
        return announce_string

    def action_delete_document(self, event):
        event.delete_this()

    def action_get_winners(self, max_points, event):
        winners = set()
        for role in event.participating_roles:
            if role.points == max_points and role.points != 0:
                for discord_user_id in role.discord_user_ids:
                    winners.add(discord_user_id)
        return list(winners)

    def action_get_points(self, event):
        max_points = 0
        gathered_points = {}
        for role in event.participating_roles:
            max_points = max(role.points, max_points)
            gathered_points[role.role_id] = role.points
        return max_points, gathered_points

    async def action_announce_winner(self, announce_string, event: Event):
        server = data_access.find_one(Server, discord_guild_id=event.discord_guild_id)
        guild = discord.utils.get(self.client.guilds, id=event.discord_guild_id)
        channel = discord.utils.get(guild.text_channels, id=server.announcement_channel_id)
        if not channel:
            channel = guild.text_channels[0]
        await channel.send(announce_string)
