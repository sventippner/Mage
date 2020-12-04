import discord

from mage.models.Server import Server
from utils import data_access
from random import randint


class Dice:
    aliases = []
    brief = 'role a dice'
    description = 'role a dice and gain or loose points'

    __item_name = "Dice"
    use_cost = 60

    @staticmethod
    async def call(context):
        """ this function is executed by a discord message """
        user = data_access.find_user_by_discord_message(context.message)
        user.name = context.author.display_name
        guild = data_access.find_one(Server, discord_guild_id=context.guild.id)

        if user.points - Dice.use_cost < 0:
            await context.send(f"You do not have enough {guild.points_name}! You need at least {Dice.use_cost}")
        else:
            role_result = randint(1, 6)
            if role_result == 6:
                amount = 100
                user.points = user.points + amount
                user.save()
                await context.send(f"Congratulations {context.author.display_name}. You roled a 6. +100 points"
                                   f" Your points now: {user.points}")

            if 4 < role_result < 6:
                amount = 40
                user.points = user.points + amount
                user.save()
                await context.send(f"{context.author.display_name} roled a {role_result}. It's getting better and better."
                                   f" Your points now: {user.points}")

            if role_result < 4:
                amount = 0
                user.points = user.points + amount
                user.save()
                await context.send(f"{context.author.display_name} roled a {role_result}. Next time it will be better! "
                                   f" Your points now: {user.points}")