from datetime import datetime, timedelta

import discord
from discord.ext import commands
from discord.ext.commands import RoleConverter

from discord_mage.commands.event.start.Now.Now import Now
from discord_mage.commands.event.start.Start import Start
from discord_mage.commands.event.Event import Event as EventCommand
from discord_mage.commands.moderation.Announcements.Announce import Announce
from mage.models.ParticipatingRole import ParticipatingRole
from discord_mage.permissions.IsGuildMessage import IsGuildMessage
from mage.models.Server import Server
from utils.data_access import find_one


class Event(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.group(aliases=EventCommand.aliases, brief=EventCommand.brief, description=EventCommand.description)
    @commands.check(IsGuildMessage.is_guild_message)
    async def event(self, context):
        await EventCommand.call(context)

    @event.group(aliases=Start.aliases, brief=Start.brief, description=Start.description)
    @commands.check(IsGuildMessage.is_guild_message)
    @commands.has_permissions(administrator=True)
    async def start(self, context):
        await Start.call(context)

    @start.command(aliases=Now.aliases, brief=Now.brief, description=Now.description)
    @commands.check(IsGuildMessage.is_guild_message)
    @commands.has_permissions(administrator=True)
    async def now(self, context, name, duration: int, rewards: str, *, participating_roles):
        announcement_channel_id = find_one(Server, discord_guild_id=context.guild.id).announcement_channel_id
        if announcement_channel_id:
            start_date = datetime.now()
            end_date = start_date + timedelta(days=duration)
            role_converter = RoleConverter()
            roles = [await role_converter.convert(context, role) for role in participating_roles.split()]
            role_participant_list = [ParticipatingRole(role.id, [member.id for member in role.members], 0) for role in roles]
            rewards = rewards.split()
            await Now.call(context, name, start_date, end_date, rewards, role_participant_list)
        else:
            await context.send(Announce.action_no_announcement_channel())


def setup(client):
    client.add_cog(Event(client))
