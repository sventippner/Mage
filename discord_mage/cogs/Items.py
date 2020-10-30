import discord
from discord.ext import commands
from discord_mage.commands.items.TestItem import TestItem


class Items(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=TestItem.aliases, brief=TestItem.brief, description=TestItem.description)
    async def testitem(self, context, target: discord.Member, amount: int = 0):

        await TestItem().call(context, target, amount)


def setup(client):
    client.add_cog(Items(client))
