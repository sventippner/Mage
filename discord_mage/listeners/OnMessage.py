import discord
from datetime import datetime

from mage.models.Event import Event
from mage.models.User import User
from mage.models.XPMultiplier import XPMultiplier
from utils import data_access


class OnMessage:
    points_per_message = 1

    @staticmethod
    async def call(message):
        # ignores its own messages
        if message.author.bot:
            return

        author = data_access.find_user_by_discord_message(message)
        if not author:
            author = User.from_discord(message.author.id, message.guild.id)
            author.save()
        if not message.content.startswith(data_access.get_prefix(message.guild.id)):
            OnMessage.action_increase_user_points(author)
            OnMessage.action_increase_event_points(message, author)

    @staticmethod
    def action_increase_user_points(user):
        xp_multiplier = data_access.find_one(XPMultiplier, discord_guild_id=user.discord_guild_id, discord_user_id=user.discord_user_id)
        multiplier = 1
        if xp_multiplier:
            if xp_multiplier.end_date > datetime.now():
                multiplier = xp_multiplier.multiplier
            else:
                xp_multiplier.delete_this()
        user.points += (OnMessage.points_per_message * multiplier)
        user.save_this(set__points=user.points)

    @staticmethod
    def action_increase_event_points(message: discord.Message, user: User):
        event = data_access.find_one(Event, discord_guild_id=user.discord_guild_id)
        if event:
            role_ids = [role.id for role in message.author.roles]
            for role in event.participating_roles:
                if role.role_id in role_ids and user.discord_user_id in role.discord_user_ids:
                    role.points += OnMessage.points_per_message
            event.save()
