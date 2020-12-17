from mage.models.Server import Server
from utils import data_access, MagicTools


class Use:
    aliases = []
    brief = 'uses items'
    description = "uses items"

    @staticmethod
    async def call(context):
        msg = "Todo"
        await context.send(msg)
