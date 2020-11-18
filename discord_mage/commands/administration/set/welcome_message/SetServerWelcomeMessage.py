from discord_mage.commands.administration.set.Set import Set
from mage.models.Server import Server
from utils import data_access


class SetServerWelcomeMessage:
    aliases = []
    brief = ""
    description = ""

    @staticmethod
    async def call_custom_server_welcome_messages(context, value):
        if value.lower() == "on" or value.lower() == "true":
            server = data_access.find_one(Server, discord_guild_id=context.guild.id)
            server.guild_welcome_message_enabled = True
            server.save()
            await context.send(Set.action_set_argument("custom_server_welcome_messages", "enabled"))
        elif value.lower() == "off" or value.lower() == "false":
            server = data_access.find_one(Server, discord_guild_id=context.guild.id)
            server.guild_welcome_message_enabled = False
            server.save()
            await context.send(Set.action_set_argument("custom_server_welcome_messages", "disabled"))
        else:
            await context.send(Set.action_invalid_argument(value))