from config import DEFAULT_PREFIX
from mage.models.Event import Event as EventModel
from mage.models.Server import Server
from utils.data_access import find_one


class Event:
    aliases = []
    brief = "event group"
    description = "event group. Can be used to invoke subcommands"

    @staticmethod
    async def call(context):
        return
