import discord
from discord.ext import commands
from discord_mage.commands.items.TestItem import TestItem
from discord_mage.commands.items.Dice import Dice
from discord_mage.commands.items.use.Use import Use
from discord_mage.permissions.IsGuildMessage import IsGuildMessage
from mage.items.ChannelLicense import ChannelLicense


class Items(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.group(aliases=Use.aliases, brief=Use.brief, description=Use.description)
    @commands.check(IsGuildMessage.is_guild_message)
    async def use(self, context, item_name):
        await Use.call(context, item_name)

    @use.command(aliases=TestItem.aliases, brief=TestItem.brief, description=TestItem.description)
    @commands.check(IsGuildMessage.is_guild_message)
    async def testitem(self, context, target: discord.Member, amount: int = 0):
        await TestItem().call(context, target, amount)

    @use.command(aliases=Dice.aliases, brief=Dice.brief, description=Dice.description)
    @commands.check(IsGuildMessage.is_guild_message)
    async def dice(self, context):
        await Dice().call(context)

    @use.command(brief=ChannelLicense.brief, description=ChannelLicense.description)
    @commands.check(IsGuildMessage.is_guild_message)
    async def channellicense(self, context, *, name):
        await ChannelLicense.on_use(context, name)


def setup(client):
    client.add_cog(Items(client))
