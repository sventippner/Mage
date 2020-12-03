import discord
from discord.ext import commands

from discord_mage.commands.administration.add.points.AddPoints import AddPoints
from discord_mage.commands.administration.set.channel.SetAnnouncementChannel import SetAnnouncementChannel
from discord_mage.commands.administration.set.channel.SetModerationChannel import SetModerationChannel
from discord_mage.commands.administration.add.welcome_message.AddPrivateWelcomeMessage import AddPrivateWelcomeMessage
from discord_mage.commands.administration.add.welcome_message.AddServerWelcomeMessage import AddServerWelcomeMessage
from discord_mage.commands.administration.set.autorole.SetAutorole import SetAutorole
from discord_mage.commands.administration.set.prefix.SetPrefix import SetPrefix
from discord_mage.commands.administration.add.Add import Add
from discord_mage.commands.administration.set.Set import Set
from discord_mage.commands.administration.set.welcome_message.SetPrivateWelcomeMessage import SetPrivateWelcomeMessage
from discord_mage.commands.administration.set.welcome_message.SetServerWelcomeMessage import SetServerWelcomeMessage
from discord_mage.permissions.IsGuildMessage import IsGuildMessage


class Administration(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.group(aliases=Add.aliases, brief=Add.brief, description=Add.description)
    @commands.check(IsGuildMessage.is_guild_message)
    @commands.has_permissions(administrator=True)
    async def add(self, context):
        await Add.call(context)

    @add.command(aliases=AddPrivateWelcomeMessage.aliases, brief=AddPrivateWelcomeMessage.brief, description=AddPrivateWelcomeMessage.description)
    @commands.check(IsGuildMessage.is_guild_message)
    @commands.has_permissions(administrator=True)
    async def custom_private_welcome_message(self, context, message_id: int):
        await AddPrivateWelcomeMessage.call_custom_private_welcome_message(context, message_id)

    @add.command(aliases=AddServerWelcomeMessage.aliases, brief=AddServerWelcomeMessage.brief, description=AddServerWelcomeMessage.description)
    @commands.check(IsGuildMessage.is_guild_message)
    @commands.has_permissions(administrator=True)
    async def custom_server_welcome_message(self, context, message_id: int):
        await AddServerWelcomeMessage.call_custom_server_welcome_message(context, message_id)

    @add.command(aliases=AddPoints.aliases, brief=AddPoints.brief, description=AddPoints.description)
    @commands.check(IsGuildMessage.is_guild_message)
    @commands.has_permissions(administrator=True)
    async def points(self, context, member: discord.Member, amount: int):
        await AddPoints.call(context, member, amount)

    @commands.group(aliases=Set.aliases, brief=Set.brief, description=Set.description)
    @commands.check(IsGuildMessage.is_guild_message)
    @commands.has_permissions(administrator=True)
    async def set(self, context):
        await Set.call(context)

    @set.command(aliases=SetPrivateWelcomeMessage.aliases, brief=SetPrivateWelcomeMessage.brief, description=SetPrivateWelcomeMessage.description)
    @commands.check(IsGuildMessage.is_guild_message)
    @commands.has_permissions(administrator=True)
    async def custom_private_welcome_messages(self, context, value):
        await SetPrivateWelcomeMessage.call_custom_private_welcome_messages(context, value)

    @set.command(aliases=SetServerWelcomeMessage.aliases, brief=SetServerWelcomeMessage.brief, description=SetServerWelcomeMessage.description)
    @commands.check(IsGuildMessage.is_guild_message)
    @commands.has_permissions(administrator=True)
    async def custom_server_welcome_messages(self, context, value):
        await SetServerWelcomeMessage.call_custom_server_welcome_messages(context, value)

    @set.command(aliases=SetAutorole.aliases, brief=SetAutorole.brief, description=SetAutorole.description)
    @commands.check(IsGuildMessage.is_guild_message)
    @commands.has_permissions(administrator=True)
    async def autorole(self, context, *, roles):
        await SetAutorole.call_autorole(context, roles)

    @set.command(aliases=SetPrefix.aliases, brief=SetPrefix.brief, description=SetPrefix.description)
    @commands.check(IsGuildMessage.is_guild_message)
    @commands.has_permissions(administrator=True)
    async def prefix(self, context, prefix):
        """
        sets command prefix
        :param context: context object automatically passed on function call
        :param prefix: new prefix
        """
        await SetPrefix.call(context, prefix)

    @set.command(aliases=SetAnnouncementChannel.aliases, brief=SetAnnouncementChannel.brief,
                      description=SetAnnouncementChannel.description)
    @commands.check(IsGuildMessage.is_guild_message)
    @commands.has_permissions(administrator=True)
    async def announcement_channel(self, context, channel: discord.TextChannel = None):
        """
        sets serverwide announcement channel other commands will use
        (if channel is not passed, the channel in which the command was sent in will become the announcementchannel instead)
        Admin permissions required
        :param context: context object automatically passed on function call
        :param channel: announcementchannel
        """
        await SetAnnouncementChannel.call(context, channel)

    @set.command(aliases=SetModerationChannel.aliases, brief=SetModerationChannel.brief,
                      description=SetModerationChannel.description)
    @commands.check(IsGuildMessage.is_guild_message)
    @commands.has_permissions(administrator=True)
    async def moderation_channel(self, context, channel: discord.TextChannel = None):
        """
        sets serverwide moderation channel other commands will use
        (if channel is not passed, the channel in which the command was sent in will become the moderationchannel instead)
        Admin permissions required
        :param context: context object automatically passed on function call
        :param channel: moderationchannel
        """
        await SetModerationChannel.call(context, channel)


def setup(client):
    client.add_cog(Administration(client))
