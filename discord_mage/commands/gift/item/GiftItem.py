import discord

from mage.models.User import User
from utils import data_access


class GiftItem:
    aliases = []
    brief = "gives corresponding item to another user"
    description = "gives corresponding item to another user"

    @staticmethod
    async def call_item(context, amount: int, item_name, member: discord.Member):
        user = data_access.find_user_by_discord_message(context.message)
        target_user = data_access.find_one(User, discord_user_id=member.id)
        if user.has_item(item_name, amount=amount):
            if not target_user:
                target_user = User(discord_user_id=member.id, discord_guild_id=context.guild.id)
            user.lose_item(item_name, amount=amount)
            target_user.obtain_item(item_name, amount=amount)
            user.save()
            target_user.save()
            await context.send(GiftItem.action_gifted_item(context, member, item_name, amount))
        else:
            await context.send(GiftItem.action_does_not_have_item(context, item_name, amount))

    @staticmethod
    def action_does_not_have_item(context, item_name, amount):
        return f"You don't have {amount}x {item_name}.\n{context.author.mention}"

    @staticmethod
    def action_gifted_item(context, member, item_name, amount):
        return f"{context.author.mention} gifts {member.mention} **{amount}x {item_name}**!"
