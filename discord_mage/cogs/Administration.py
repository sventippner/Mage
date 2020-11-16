import discord
from discord.ext import commands

from discord_mage.commands.SetAnnouncementChannel import SetAnnouncementChannel
from discord_mage.commands.SetModerationChannel import SetModerationChannel
from discord_mage.commands.SetPrefix import SetPrefix
from discord_mage.commands.administration.Add import Add
from discord_mage.commands.administration.Set import Set


class Administration(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.group(aliases=Set.aliases, brief=Set.brief, description=Set.description)
    @commands.has_permissions(administrator=True)
    async def set(self, context):
        print("set")

    @set.command()
    @commands.has_permissions(administrator=True)
    async def custom_private_welcome_messages(self, context, value):
        await Set.call_custom_private_welcome_messages(context, value)

    @set.command()
    @commands.has_permissions(administrator=True)
    async def custom_server_welcome_messages(self, context, value):
        await Set.call_custom_server_welcome_messages(context, value)\


    @commands.group(aliases=Add.aliases, brief=Add.brief, description=Add.description)
    @commands.has_permissions(administrator=True)
    async def add(self, context):
        print("add")

    @add.command()
    @commands.has_permissions(administrator=True)
    async def custom_private_welcome_message(self, context, message_id: int):
        await Add.call_custom_private_welcome_message(context, message_id)

    @add.command()
    @commands.has_permissions(administrator=True)
    async def custom_server_welcome_message(self, context, message_id: int):
        await Add.call_custom_server_welcome_message(context, message_id)



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
