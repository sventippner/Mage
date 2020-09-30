from discord.ext import commands
from discord_mage.commands import Hello


class Test(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=Hello.Hello.aliases, brief=Hello.Hello.brief, description=Hello.Hello.description)
    async def hello(self, context):
        await context.send(f'Hello! {context.author.mention}')


def setup(client):
    print(Hello.Hello.brief)
    client.add_cog(Test(client))
