import discord
from discord.ext import commands

from discord_mage.commands.SetAnnouncementChannel import SetAnnouncementChannel
from discord_mage.commands.SetModerationChannel import SetModerationChannel
from discord_mage.commands.SetPrefix import SetPrefix


class Administration(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=SetPrefix.aliases, brief=SetPrefix.brief, description=SetPrefix.description)
    @commands.has_permissions(administrator=True)
    async def set_prefix(self, context, prefix):
        """
        sets command prefix
        :param context: context object automatically passed on function call
        :param prefix: new prefix
        """
        await SetPrefix.call(context, prefix)

    @commands.command(aliases=SetAnnouncementChannel.aliases, brief=SetAnnouncementChannel.brief,
                      description=SetAnnouncementChannel.description)
    @commands.has_permissions(administrator=True)
    async def set_announcement_channel(self, context, channel: discord.TextChannel = None):
        """
        sets serverwide announcement channel other commands will use
        (if channel is not passed, the channel in which the command was sent in will become the announcementchannel instead)
        Admin permissions required
        :param context: context object automatically passed on function call
        :param channel: announcementchannel
        """
        await SetAnnouncementChannel.call(context, channel)

    @commands.command(aliases=SetModerationChannel.aliases, brief=SetModerationChannel.brief,
                      description=SetModerationChannel.description)
    @commands.has_permissions(administrator=True)
    async def set_moderation_channel(self, context, channel: discord.TextChannel = None):
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
