import discord

from mage.models.User import User
from utils import data_access


class Gift:
    aliases = ['give']
    brief = "gives something to another user"
    description = "gives something to another user"

    @staticmethod
    async def call_gift():
        return
