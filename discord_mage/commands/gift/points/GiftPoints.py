import discord

from mage.models.User import User
from utils import data_access


class GiftPoints:
    aliases = []
    brief = "gives points to another user"
    description = "gives points to another user"

    @staticmethod
    async def call_points(context, points: int, member: discord.Member):
        user = data_access.find_user_by_discord_message(context.message)
        target_user = data_access.find_one(User, discord_user_id=member.id)
        if points > user.points:
            msg = GiftPoints.action_insufficient_points(points, user.points)
            await context.send(msg)
        else:
            msg = await GiftPoints.action_gift_points(context, member, user, target_user, points)
            await context.send(msg)

    @staticmethod
    async def action_gift_points(context, member: discord.Member, user, target_user, points: int):
        user.points -= points
        user.save_this(set__points=user.points)
        target_user.points += points
        target_user.save_this(set__points=target_user.points)
        msg = f"{context.author.mention} gifts {member.mention} **{points}** points!"
        return msg

    @staticmethod
    def action_insufficient_points(amount, max_user_points):
        return f"{amount} is an invalid input. The Amount must be between 1 and {max_user_points}."
