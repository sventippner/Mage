from discord_mage.commands.administration.add.welcome_message.AddWelcomeMessage import AddWelcomeMessage
from mage.models.Server import Server
from utils import data_access


class AddServerWelcomeMessage:
    aliases = []
    brief = ""
    description = ""

    @staticmethod
    async def call_custom_server_welcome_message(context, message_id: int):
        msg = await context.channel.fetch_message(message_id)
        msg = msg.content
        server = data_access.find_one(Server, discord_guild_id=context.guild.id)
        server.guild_welcome_messages.append(msg)
        server.save()
        await context.send(AddWelcomeMessage.action_added_message())