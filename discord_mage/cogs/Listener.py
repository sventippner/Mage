from discord.ext import commands

from discord_mage.listeners.OnMessage import OnMessage
from discord_mage.listeners.OnReady import OnReady
from discord_mage.listeners.OnCommandError import OnCommandError


class Listener(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        """will be executed after boot once bot is ready"""
        OnReady().call(self.client)


    @commands.Cog.listener()
    async def on_command_error(self, context, error):
        """
        will be executed if an error is raised within a command
        :param context: context object automatically passed on function call
        :param error: raised error
        """
        await OnCommandError().call(context, error)

    @commands.Cog.listener()
    async def on_message(self, message):
        await OnMessage().call(self.client, message)


def setup(client):
    client.add_cog(Listener(client))
