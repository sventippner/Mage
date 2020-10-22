from discord.ext import commands
from discord_mage.commands.Purge import Purge


class Moderation(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(brief=Purge.brief, description=Purge.description)
    @commands.has_permissions(manage_messages=True)
    async def purge(self, context, amount=2):
        await Purge.call(context, amount)


def setup(client):
    client.add_cog(Moderation(client))

