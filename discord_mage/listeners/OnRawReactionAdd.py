import discord

from mage.models.Message import Message
from utils import data_access


class OnRawReactionAdd:

    @staticmethod
    async def call(client, reaction: discord.RawReactionActionEvent):
        if reaction.user_id == client.user.id:
            return
        db_message = data_access.find_one(Message, discord_message_id=reaction.message_id)
        if db_message:
            channel = await client.fetch_channel(reaction.channel_id)
            message = await channel.fetch_message(reaction.message_id)
            for db_reaction in db_message.reactions:
                if str(reaction.emoji) == db_reaction.emoji:
                    await OnRawReactionAdd.action_toggle_role(reaction, client, db_reaction.role_id, db_message)
            await message.remove_reaction(reaction.emoji, reaction.member)

    @staticmethod
    async def action_toggle_role(reaction, client, role_id, db_message):
        guild = discord.Client.get_guild(client, reaction.guild_id)
        discord_role = guild.get_role(role_id)
        if discord_role in reaction.member.roles:
            await discord.Member.remove_roles(reaction.member, discord_role)
        else:
            if db_message.is_distinct:
                for db_reaction in db_message.reactions:
                    role_id = db_reaction.role_id
                    role_to_remove = guild.get_role(role_id)
                    await discord.Member.remove_roles(reaction.member, role_to_remove)
            await discord.Member.add_roles(reaction.member, discord_role)
