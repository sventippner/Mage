from mongoengine import Document, StringField, DateTimeField, IntField, ListField


# todo: rewards

class Event(Document):
    """ Event
    :param start_date: DateTime when the event started.
    :param end_date = DateTime when the event ends.
    :param duration = DateTime how long the event lasts.
    :param reward = Rewards
    """

    discord_guild_id = IntField()
    name = StringField()

    start_date = DateTimeField()
    end_date = DateTimeField()
    # duration = DateTimeField()

    # list of role ids
    role_restriction = ListField(IntField())
    participants = ListField(IntField())

    reward = IntField()
