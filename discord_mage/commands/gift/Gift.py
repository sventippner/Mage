import discord

from mage.models.User import User
from utils import data_access


class Gift:
    aliases = ['give']
    brief = "gives something to another user"
    description = "gives something to another user"

    @staticmethod
    async def call_gift():
        print("gifting call")  # TODO gifting call without subcommands

    @staticmethod
    async def call_points(context, points: int, member: discord.Member):
        user = data_access.find_user_by_discord_message(context.message)
        target_user = data_access.find_one(User, discord_user_id=member.id)
        if points > user.points:
            msg = Gift.action_insufficient_points(points, user.points)
            await context.send(msg)
        else:
            msg = await Gift.action_gift_points(context, member, user, target_user, points)
            await context.send(msg)

    @staticmethod
    async def call_item(context, amount: int, item_id: int, member: discord.Member):
        user = data_access.find_user_by_discord_message(context.message)
        target_user = data_access.find_one(User, discord_user_id=member.id)
        if user.has_item(item_id, amount=amount):
            if not target_user:
                target_user = User(discord_user_id=member.id, discord_guild_id=context.guild.id)
            user.lose_item(item_id, amount=amount)
            target_user.obtain_item(item_id, amount=amount)
            user.save()
            target_user.save()
            await context.send(Gift.action_gifted_item(context, member, item_id, amount))
        else:
            await context.send(Gift.action_does_not_have_item(context, item_id, amount))

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

    @staticmethod
    def action_does_not_have_item(context, item, amount):
        return f"You don't have {amount}x {item}.\n{context.author.mention}"

    @staticmethod
    def action_gifted_item(context, member, item_id, amount):
        return f"{context.author.mention} gifts {member.mention} **{amount}x {item_id}**!"
