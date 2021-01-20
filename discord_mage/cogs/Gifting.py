import discord
from discord.ext import commands

from discord_mage.commands.gift.Gift import Gift
from discord_mage.commands.gift.item.GiftItem import GiftItem
from discord_mage.commands.gift.points.GiftPoints import GiftPoints
from discord_mage.permissions.IsGuildMessage import IsGuildMessage


class Gifting(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.group(aliases=Gift.aliases, brief=Gift.brief, description=Gift.description)
    @commands.check(IsGuildMessage.is_guild_message)
    async def gift(self, context):
        await Gift.call_gift()

    @gift.group(aliases=GiftPoints.aliases, brief=GiftPoints.brief, description=GiftPoints.description)
    @commands.check(IsGuildMessage.is_guild_message)
    async def points(self, context, points: int, member: discord.Member):
        await GiftPoints.call_points(context, points, member)

    @gift.group(aliases=GiftItem.aliases, brief=GiftItem.brief, description=GiftItem.description)
    @commands.check(IsGuildMessage.is_guild_message)
    async def item(self, context, amount: int, item, member: discord.Member):
        await GiftItem.call_item(context, amount, item, member)


def setup(client):
    client.add_cog(Gifting(client))
