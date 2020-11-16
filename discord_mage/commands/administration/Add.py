import discord

from config import DEFAULT_PREFIX
from mage.models.Server import Server
from utils import data_access


class Add:
    aliases = []
    brief = 'adds values'
    description = "adds values"

    @staticmethod
    async def call_custom_private_welcome_message(context, message_id: int):
        msg = context.get_message(message_id).content
        server = data_access.find_one(Server, discord_guild_id=context.guild.id)
        server.personal_welcome_messages.append(msg)
        server.save()
        await context.send(Add.action_added_message())

    @staticmethod
    async def call_custom_server_welcome_message(context, message_id: int):
        msg = await context.channel.fetch_message(message_id)
        msg = msg.content
        server = data_access.find_one(Server, discord_guild_id=context.guild.id)
        server.guild_welcome_messages.append(msg)
        server.save()
        await context.send(Add.action_added_message())

    @staticmethod
    def action_added_message():
        return "message has been added."
