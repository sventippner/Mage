import discord
from discord.ext import commands

from discord_mage.commands.gift.Gift import Gift


class Gifting(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.group(aliases=Gift.aliases, brief=Gift.brief, description=Gift.description)
    async def gift(self, context):
        await Gift.call_gift()

    @gift.group()
    async def points(self, context, points: int, member: discord.Member):
        await Gift.call_points(context, points, member)

    @gift.group()
    async def item(self, context):
        print("TODO gift item to another user")  # TODO: gift items


def setup(client):
    client.add_cog(Gifting(client))
