from discord.ext.commands import RoleConverter

from mage.models.Server import Server
from utils import data_access


class SetAutorole:
    aliases = []
    brief = ""
    description = ""

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
