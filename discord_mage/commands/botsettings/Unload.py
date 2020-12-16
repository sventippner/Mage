import discord.ext

from config import COGS_PATHS


class Unload:
    aliases = []
    brief = "unloads cog"
    description = "unloads specified cog extension"

    @staticmethod
    async def call(context, client, extension):
        for cogs_path in COGS_PATHS:
            try:
                client.unload_extension(str(cogs_path).replace('\\', '.').replace('/', '.') + f'.{extension}')
                await context.send(Unload.action_success(extension))
            except discord.ext.commands.errors.ExtensionNotLoaded:
                await context.send(Unload.action_not_found(extension))

    @staticmethod
    def action_success(extension):
        return f'Extension **{extension}** has been unloaded successfully'

    @staticmethod
    def action_not_found(extension):
        return f'Extension **{extension}** has not been found in this path.'
