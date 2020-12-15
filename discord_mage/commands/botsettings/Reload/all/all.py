from config import COGS_PATHS
from utils.Extensions import Extensions


class all:
    aliases = []
    brief = "reloads all cogs"
    description = "reloads all cog extensions"

    @staticmethod
    async def call(context, client):
        Extensions.unload_extensions(client, COGS_PATHS)
        Extensions.load_extensions(client, COGS_PATHS)
        await context.send(all.action_done())

    @staticmethod
    def action_done():
        return f'Done'

    @staticmethod
    def action_success(extension):
        return f'Extension **{extension}** has been reloaded successfully'
