
from discord.ext import commands

from discord_mage.commands.shop.BuyItem import BuyItem
from discord_mage.commands.shop.Shop import Shop
from discord_mage.permissions.IsGuildMessage import IsGuildMessage


class Points(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=BuyItem.aliases, brief=BuyItem.brief, description=BuyItem.description)
    @commands.check(IsGuildMessage.is_guild_message)
    async def buyitem(self, context, *, item_name):
        await BuyItem.call(context, item_name)

    @commands.command(aliases=Shop.aliases, brief=Shop.brief, description=Shop.description)
    @commands.check(IsGuildMessage.is_guild_message)
    async def shop(self, context):
        await Shop.call(context)


def setup(client):
    client.add_cog(Points(client))
