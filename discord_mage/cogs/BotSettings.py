import os

from discord.ext import commands

from discord_mage.commands.botsettings.Reload.Reload import Reload
from discord_mage.commands.botsettings.Reload.all.all import all
from discord_mage.commands.botsettings.Unload import Unload
from discord_mage.commands.botsettings.Load import Load
from discord_mage.permissions.IsBotOwner import IsBotOwner
from discord_mage.permissions.IsGuildMessage import IsGuildMessage
from config import COGS_PATHS


class BotSettings(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=Load.aliases, brief=Load.brief, description=Load.description)
    @commands.check(IsGuildMessage.is_guild_message)
    @commands.check(IsBotOwner.is_bot_owner)
    async def load(self, context, extension):
        await Load.call(context, self.client, extension)

    @commands.command(aliases=Unload.aliases, brief=Unload.brief, description=Unload.description)
    @commands.check(IsGuildMessage.is_guild_message)
    @commands.check(IsBotOwner.is_bot_owner)
    async def unload(self, context, extension):
        await Unload.call(context, self.client, extension)

    @commands.group(invoke_without_command=True, brief=Reload.brief, description=Reload.description)
    @commands.check(IsGuildMessage.is_guild_message)
    @commands.check(IsBotOwner.is_bot_owner)
    async def reload(self, context, extension):
        if context.invoked_subcommand is None:
            await Reload.call(context, self.client, extension)

    @reload.command(aliases=Reload.aliases, brief=all.brief, description=all.description)
    @commands.check(IsGuildMessage.is_guild_message)
    @commands.check(IsBotOwner.is_bot_owner)
    async def all(self, context):
        await all.call(context, self.client)


def setup(client):
    client.add_cog(BotSettings(client))
