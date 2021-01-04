import discord
from discord.ext import commands
from discord_mage.commands.items.use.Use import Use
from discord_mage.permissions.IsGuildMessage import IsGuildMessage
from mage.items.ChannelLicense import ChannelLicense
from mage.items.Dice import Dice


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

    @use.command(brief=ChannelLicense.brief, description=ChannelLicense.description)
    @commands.check(IsGuildMessage.is_guild_message)
    async def channellicense(self, context, *, name):
        await ChannelLicense.on_use(context, name)


def setup(client):
    client.add_cog(Items(client))
