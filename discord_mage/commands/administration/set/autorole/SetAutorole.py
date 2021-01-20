from discord.ext.commands import RoleConverter

from mage.models.Server import Server
from utils import data_access


class SetAutorole:
    aliases = []
    brief = "sets roles, which members automatically join upon joining the server"
    description = "sets roles, which members automatically join upon joining the server"

    @staticmethod
    async def call_autorole(context, roles):
        excluded = ['@everyone', '@here']
        if any(word in roles for word in excluded):
            await context.send(f"Arguments contain ineligible role(s).")
        else:
            role_converter = RoleConverter()
            server = data_access.find_one(Server, discord_guild_id=context.guild.id)
            new_autoroles = []
            for role in roles.split():
                discord_role = await role_converter.convert(context, role)
                if discord_role.name not in excluded:
                    new_autoroles.append(discord_role.id)
                else:
                    await context.send(f"{discord_role.name} is not a viable role and will be excluded in autorole.\n")
            server.autorole_role_ids = new_autoroles
            server.save()
            await context.send(f"New Members now join the following roles automatically when joining the server:\n{roles if roles else 'No Roles selected'}")
