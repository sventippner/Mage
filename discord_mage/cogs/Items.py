import discord
from discord.ext import commands
from discord_mage.commands.items.use.Use import Use
from discord_mage.permissions.IsGuildMessage import IsGuildMessage
from mage.items.ChannelLicense import ChannelLicense
from mage.items.Dice import Dice
from mage.items.PointBoost import PointBoost
from mage.items.PointBoost2x7days import PointBoost2x7days
from mage.items.PointBoost2x30days import PointBoost2x30days
from mage.items.PointBoost4x1day import PointBoost4x1day
from mage.items.Coin import Coin


class Items(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.group(aliases=Use.aliases, brief=Use.brief, description=Use.description)
    @commands.check(IsGuildMessage.is_guild_message)
    async def use(self, context):
        if context.invoked_subcommand is None:
            await Use.call(context)

    @use.command(brief=Dice.brief, description=Dice.description)
    @commands.check(IsGuildMessage.is_guild_message)
    async def dice(self, context):
        await Dice().on_use(context)

    @use.command(brief=Coin.brief, description=Coin.description)
    @commands.check(IsGuildMessage.is_guild_message)
    async def coin(self, context):
        await Coin().on_use(context)

    @use.command(brief=ChannelLicense.brief, description=ChannelLicense.description)
    @commands.check(IsGuildMessage.is_guild_message)
    async def channellicense(self, context, *, name):
        await ChannelLicense.on_use(context, name)

    @use.command(brief=PointBoost.brief, description=PointBoost.description)
    @commands.check(IsGuildMessage.is_guild_message)
    async def pointboost(self, context):
        await PointBoost.on_use(context)

    @use.command(brief=PointBoost2x7days.brief, description=PointBoost2x7days.description)
    @commands.check(IsGuildMessage.is_guild_message)
    async def pointboost2x7days(self, context):
        await PointBoost2x7days.on_use(context)

    @use.command(brief=PointBoost2x30days.brief, description=PointBoost2x30days.description)
    @commands.check(IsGuildMessage.is_guild_message)
    async def pointboost2x30days(self, context):
        await PointBoost2x30days.on_use(context)

    @use.command(brief=PointBoost4x1day.brief, description=PointBoost4x1day.description)
    @commands.check(IsGuildMessage.is_guild_message)
    async def pointboost4x1day(self, context):
        await PointBoost4x1day.on_use(context)


def setup(client):
    client.add_cog(Items(client))
