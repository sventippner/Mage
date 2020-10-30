from itertools import cycle

from config import DEFAULT_PREFIX

import discord
from discord.ext import tasks, commands


class ChangeStatus():

    def __init__(self, client):
        self.client = client
        self.all_commands = cycle((
            f'{DEFAULT_PREFIX}{command} {command.brief}' if command.brief else f'{DEFAULT_PREFIX}{command}'
            for command in self.client.commands))

    @tasks.loop(seconds=10)
    async def call(self):
        await self.client.change_presence(activity=discord.Game(f'{next(self.all_commands)}'))