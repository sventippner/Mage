from config import DEFAULT_PREFIX
from mage.models.Event import Event
from mage.models.Server import Server
from utils.data_access import find_one


class StartEvent:
    aliases = ['startnow']
    brief = "starts custom event"
    description = "starts a custom event with a specified reward"

    @staticmethod
    async def call(context, name, start_date, end_date, rewards, participating_roles, participants=None):
        event = Event(context.guild.id, name, start_date, end_date, participating_roles, rewards, list(participants))
        print(participating_roles)
        print(rewards)
        event.save()
        print(event)
