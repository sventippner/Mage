from config import DEFAULT_PREFIX
from mage.models.Event import Event
from mage.models.Server import Server
from utils.data_access import find_one


class Start:
    aliases = []
    brief = "event start group"
    description = "event start group. Can be used to invoke subcommands such as 'now'"

    @staticmethod
    async def call(context):
        return
