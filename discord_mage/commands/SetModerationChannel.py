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
        if SetModerationChannel.action_is_valid(context, channel):
            await SetModerationChannel.action_set_channel(context, channel.id)
        else:
            await context.send(SetModerationChannel.action_not_valid())

    @staticmethod
    async def action_set_channel(context, channel_id):
        guild = find_one(Server, discord_guild_id=context.guild.id)
        guild.moderation_channel_id = channel_id
        guild.save()
        await context.send('Moderation channel has been changed.')

    @staticmethod
    def action_is_valid(context, channel):
        if channel in context.guild.text_channels:
            return True
        else:
            return False

    @staticmethod
    async def action_not_valid():
        return 'Invalid channel.'
