from discord.ext import commands
from discord_mage.commands.SetPrefix import SetPrefix


class Administration(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=SetPrefix.aliases, brief=SetPrefix.brief, description=SetPrefix.description)
    @commands.has_permissions(administrator=True)
    async def set_prefix(self, context, prefix):
        await SetPrefix.call(context, prefix)


def setup(client):
    client.add_cog(Administration(client))
