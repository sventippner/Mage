from discord.ext.commands import RoleConverter

from config import DEFAULT_PREFIX
from mage.models.Server import Server
from utils import data_access


class Set:
    aliases = ['switch']
    brief = 'sets values'
    description = "sets values"

    @staticmethod
    async def call(context):
        return

    @staticmethod
    def action_invalid_argument(argument):
        return f"{argument} is an invalid argument"

    @staticmethod
    def action_set_argument(argument, value):
        return f"{argument} are now {value}"
