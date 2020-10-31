
from discord.ext import commands

from discord_mage.commands.BuyItem import BuyItem
from discord_mage.commands.Shop import Shop


class Points(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=BuyItem.aliases, brief=BuyItem.brief, description=BuyItem.description)
    async def buyitem(self, context, item_name):
        await BuyItem.call(context, item_name)

    @commands.command(aliases=Shop.aliases, brief=Shop.brief, description=Shop.description)
    async def shop(self, context):
        await Shop.call(context)


def setup(client):
    client.add_cog(Points(client))
