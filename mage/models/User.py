from mongoengine import StringField, Document, LongField, IntField, ListField


class User(Document):
    """ User

    :param discord_user_id: Id of discord account
    :param discord_guild_id: Id of discord server
    :param points: amount of points the user with interactions and events
    :param items: list of items (item ids) the user has
    :param pvp_status: numeric flag of pvp status
    """
    discord_user_id = StringField(regex=r"\d")
    discord_guild_id = ListField(StringField(regex=r"\d"))
    points = LongField()
    items = ListField(IntField())
    pvp_status = IntField()

    def __init__(self):
        pass

    def __str__(self):
        return f"User ID:{self.discord_user_id} ({self.points} Points)"
