from config import DEFAULT_PREFIX
from mage.models.Event import Event
from mage.models.Server import Server
from utils.data_access import find_one


class StartEvent:
    aliases = []
    brief = "starts custom event"
    description = "starts a custom event with a specified reward"

    @staticmethod
    async def call(context, name, start_date, end_date, rewards, participating_roles):
        event = Event(context.guild.id, name, start_date, end_date, rewards, participating_roles)
        event.save()
