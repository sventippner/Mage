from discord.ext import commands
from discord_mage.commands.server.Ping import Ping


class Server(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(brief=Ping.brief, description=Ping.description)
    async def ping(self, context):
        await Ping.call(self, context)

def setup(client):
    client.add_cog(Server(client))