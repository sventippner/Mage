from discord.ext import commands
from discord_mage.commands.Hello import Hello


class Test(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=Hello.aliases, brief=Hello.brief, description=Hello.description)
    async def hello(self, context):
        await Hello().call(context)


def setup(client):
    client.add_cog(Test(client))
