import os
from pathlib import Path

import discord.ext

from config import COGS_PATHS, ROOT_DIR
from discord_mage.commands.botsettings.Load import Load
from discord_mage.commands.botsettings.Unload import Unload
from utils.Extensions import Extensions


class Reload:
    aliases = []
    brief = "reloads cog"
    description = "reloads specified cog extension"

    @staticmethod
    async def call(context, client, extension):
        for path in COGS_PATHS:
            try:
                client.unload_extension(str(path).replace('\\', '.').replace('/', '.') + f'.{extension}')
                client.load_extension(str(path).replace('\\', '.').replace('/', '.') + f'.{extension}')
                await context.send(Reload.action_success(extension))
            except discord.ext.commands.errors.ExtensionNotFound:
                await context.send(Load.action_failed(extension))
            except discord.ext.commands.errors.ExtensionNotLoaded:
                await context.send(Unload.action_not_found(extension))

    @staticmethod
    def action_done():
        return f'Done'

    @staticmethod
    def action_success(extension):
        return f'Extension **{extension}** has been reloaded successfully'
