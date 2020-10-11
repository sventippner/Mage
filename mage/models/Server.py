from mongoengine import StringField, DateField, Document


# todo: events
# todo: date_joined

class Server(Document):
    """ Server

    :param discord_guild_id: Discord Server Id
    :param date_joined: Date on which the bot joined the server.
    :param bot_prefix: Prefix for commands
    :param announcement_channel_id: Discord Channel Id for announcement messages.
    """
    discord_guild_id = StringField(regex=r"\d")
    date_joined = DateField()
    bot_prefix = StringField(min_length=1, max_length=3)
    announcement_channel_id = StringField(regex=r"\d")
