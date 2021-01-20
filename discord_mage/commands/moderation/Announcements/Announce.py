from config import DEFAULT_PREFIX
from mage.models.Server import Server
from utils.data_access import find_one


class Announce:
    aliases = []
    brief = "announce message @everyone"
    description = "make this bot announce your message @everyone in the specified announcement channel"

    @staticmethod
    async def call(context, client, message):
        announcement_channel_id = find_one(Server, discord_guild_id=context.guild.id).announcement_channel_id
        if announcement_channel_id:
            await Announce.action_announce(context, client, announcement_channel_id, message)
        else:
            await context.send(Announce.action_no_announcement_channel())

    @staticmethod
    async def action_announce(context, client, channel_id, message):
        channel = client.get_channel(channel_id)
        await channel.send(message + "\n@everyone")
        await context.message.delete()

    @staticmethod
    def action_no_announcement_channel():
        return f'An announcement channel has not been set yet.\nPlease set an announcement channel with `{DEFAULT_PREFIX}set announcementchannel` and try again.'
