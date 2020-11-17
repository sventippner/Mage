from discord.ext.commands import RoleConverter

from config import DEFAULT_PREFIX
from mage.models.Server import Server
from utils import data_access


class Set:
    aliases = ['switch']
    brief = 'sets values'
    description = "sets values"

    @staticmethod
    async def call_custom_private_welcome_messages(context, value):
        if value.lower() == "on" or value.lower() == "true":
            server = data_access.find_one(Server, discord_guild_id=context.guild.id)
            server.personal_welcome_message_enabled = True
            server.save()
            await context.send(Set.action_set_argument("custom_private_welcome_messages", "enabled"))
        elif value.lower() == "off" or value.lower() == "false":
            server = data_access.find_one(Server, discord_guild_id=context.guild.id)
            server.personal_welcome_message_enabled = False
            server.save()
            await context.send(Set.action_set_argument("custom_private_welcome_messages", "disabled"))
        else:
            await context.send(Set.action_invalid_argument(value))

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

    @staticmethod
    async def call_autorole(context, roles):
        role_converter = RoleConverter()
        server = data_access.find_one(Server, discord_guild_id=context.guild.id)
        new_autoroles = []
        for role in roles.split():
            discord_role = await role_converter.convert(context, role)
            new_autoroles.append(discord_role.id)
        server.autorole_role_ids = new_autoroles
        server.save()
        await context.send(f"New Members now join the following roles automatically when joining the server:\n{roles}")

    @staticmethod
    def action_invalid_argument(argument):
        return f"{argument} is an invalid argument"

    @staticmethod
    def action_set_argument(argument, value):
        return f"{argument} are now {value}"
