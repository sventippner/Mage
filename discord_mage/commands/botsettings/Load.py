import discord.ext

from config import COGS_PATHS
from utils.Extensions import Extensions


class Load:
    aliases = []
    brief = "loads cog"
    description = "loads specified cog extension"

    @staticmethod
    async def call(context, client, extension):
        for path in COGS_PATHS:
            try:
                client.load_extension(str(path).replace('\\', '.').replace('/', '.') + f'.{extension}')
                await context.send(Load.action_success(extension))
            except discord.ext.commands.errors.ExtensionNotFound:
                await context.send(Load.action_failed(extension))

    @staticmethod
    def action_success(extension):
        return f'Extension **{extension}** has been loaded successfully'

    @staticmethod
    def action_failed(extension):
        return f'Extension **{extension}** has not been found.'
