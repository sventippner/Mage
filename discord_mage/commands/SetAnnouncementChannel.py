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
        await SetAnnouncementChannel.action(context, channel.id)

    @staticmethod
    async def action(context, channel_id):
        guild = find_one(Server, discord_guild_id=context.guild.id)
        guild.announcement_channel_id = channel_id
        guild.save()
        await context.send('Announcement channel has been changed.')  # todo: catch invalid channel ids
