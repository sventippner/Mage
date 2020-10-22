from config import DEFAULT_PREFIX
from mage.models.Server import Server
from utils.data_access import find_one


class SetModerationChannel:
    aliases = ['setmoderationchannel']
    brief = 'sets moderation channel'
    description = f"sets a moderation channel"

    @staticmethod
    async def call(context, channel):
        if not channel:
            channel = context.channel
        await SetModerationChannel.action(context, channel.id)

    @staticmethod
    async def action(context, channel_id):
        guild = find_one(Server, discord_guild_id=context.guild.id)
        guild.moderation_channel_id = channel_id
        guild.save()
        await context.send('Moderation channel has been changed.')  # todo: catch invalid channel ids
