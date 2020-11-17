from mongoengine import StringField, DateField, Document, NotUniqueError, IntField, BooleanField, ListField
from datetime import datetime
import discord

from config import DEFAULT_PREFIX


# todo: events
# todo: date_joined

class Server(Document):
    """ Server

    :param discord_guild_id: Discord Server Id
    :param date_joined: Date on which the bot joined the server.
    :param bot_prefix: Prefix for commands
    :param announcement_channel_id: Discord Channel Id for announcement messages.
    :param moderation_channel_id: Discord Channel Id for moderation messages.
    """
    discord_guild_id = IntField(unique=True)
    server_name = StringField()
    date_joined = DateField(default=datetime.now())
    bot_prefix = StringField(min_length=1, max_length=3, default=DEFAULT_PREFIX)
    points_name = StringField()
    personal_welcome_message_enabled = BooleanField(default=False)
    guild_welcome_message_enabled = BooleanField(default=False)
    personal_welcome_messages = ListField(StringField(), default=[])
    guild_welcome_messages = ListField(StringField(), default=[])
    announcement_channel_id = IntField()
    moderation_channel_id = IntField()
    autorole_role_ids = ListField(IntField(), default=[])

    def __init__(self, guild: discord.Guild = None, *args, **kwargs):
        super(Server, self).__init__(*args, **kwargs)
        if guild:
            self.discord_guild_id = guild.id

    def delete_this(self):
        """ Deletes self document

        :return: Amount of deleted documents
        """
        return Server.objects(
            discord_guild_id=self.discord_guild_id
        ).delete()
