import discord

from mage.items.GivePoints import GivePoints
from mage.models.User import User
from utils import data_access


class TestItem:
    aliases = GivePoints.aliases
    brief = 'give points'
    description = 'gibt einem user punkte. kostet was'

    __item_name = "TestItem"
    use_cost = 25

    @staticmethod
    async def call(context, target: discord.Member, amount: int = 0):
        """ this function is executed by a discord message """
        user = data_access.find_user_by_discord_message(context.message)
        user.name = context.author.display_name

        user_target = data_access.find_one(User, discord_user_id=target.id, discord_guild_id=target.guild.id)
        user_target.name = target.display_name

        result = GivePoints.action(user, user_target, amount)
        await context.send(f"{context.author.display_name} gibt {target.display_name} {amount} Punkte")
