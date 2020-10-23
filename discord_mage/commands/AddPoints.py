import discord

from mage.models.User import User
from utils import data_access


class AddPoints:
    aliases = ['addpoints']
    brief = "adds points to mentioned users account"
    description = "adds specified amount of points to mentioned users account. Amount of points automatically reduces to match max_level for user if amount of points exceeds points needed for max_level."

    @staticmethod
    async def call(context, member: discord.Member, amount: int):
        if amount < 1:
            await context.send(AddPoints.action_zero_or_lower(amount))
        else:
            output = ""
            user = data_access.find_one(User, discord_user_id=member.id, discord_guild_id=context.guild.id)
            if not user:
                user = User.from_discord(member.id, context.guild.id)
                user.save()
            current_points = user.points
            max_points = User.level_generator[User.max_level] - current_points
            if amount > max_points:
                output += AddPoints.action_exceeds_max_points(amount, member)
                amount = max_points
            await AddPoints.action_add_points(context, output, user, member, amount)

    @staticmethod
    def action_zero_or_lower(amount):
        return f"{amount} is an invalid input. The Amount must be between 1 and {User.level_generator[User.max_level]}."

    @staticmethod
    def action_exceeds_max_points(amount, member: discord.Member):
        return f"{amount} exceeds the maximum. {member.mention} will be set to Level {User.max_level} instead.\n\n"

    @staticmethod
    async def action_add_points(context, output, user, member: discord.Member, amount):
        user.points += amount
        user.save()
        output += f"{member.mention} gained {amount} points."
        await context.send(output)
