from config import DEFAULT_PREFIX
from mage.models.Server import Server
from utils.data_access import find_one


class SetAnnouncementChannel:
    aliases = ['setannouncementchannel']
    brief = 'sets announcement channel'
    description = f"sets an announcement channel for some other commands like {DEFAULT_PREFIX}announce"

    @staticmethod
    async def call(context, channel):
        if not channel:
            channel = context.channel
        if SetAnnouncementChannel.action_is_valid(context, channel):
            await SetAnnouncementChannel.action_set_channel(context, channel.id)
        else:
            await context.send(SetAnnouncementChannel.action_not_valid())

    @staticmethod
    async def action_set_channel(context, channel_id):
        guild = find_one(Server, discord_guild_id=context.guild.id)
        guild.announcement_channel_id = channel_id
        guild.save()
        await context.send('Announcement channel has been changed.')

    @staticmethod
    def action_is_valid(context, channel):
        if channel in context.guild.text_channels:
            return True
        else:
            return False

    @staticmethod
    async def action_not_valid():
        return 'Invalid channel.'
