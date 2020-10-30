from discord.ext import commands
from discord_mage.commands.Hello import Hello


class Test(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=Hello.aliases, brief=Hello.brief, description=Hello.description)
    async def hello(self, context):
        await Hello().call(context)

    @commands.command()
    async def test(self, context):

        msg = await context.fetch_message(771735185195532358)
        o = msg.encode('unicode_escape')
        print(o)

        await context.send(o)

    @commands.command()
    async def react(self, context):
        await context.message.add_reaction('\U0001f602')
        await context.message.add_reaction('<:fat_laugh:718108247164452935>')



def setup(client):
    client.add_cog(Test(client))
