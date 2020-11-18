import discord

from config import DEFAULT_PREFIX
from mage.models.Server import Server
from utils import data_access


class Add:
    aliases = []
    brief = 'adds values'
    description = "adds values"

    @staticmethod
    async def call(context):
        print("add")
