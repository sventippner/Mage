from mongoengine import Document, StringField, DateTimeField, IntField, ListField
from datetime import datetime, timedelta


# todo: rewards

class Event(Document):
    """ Event
    :param start_date: DateTime when the event started.
    :param end_date = DateTime when the event ends.
    :param duration = DateTime how long the event lasts.
    :param rewards = Rewards
    """

    discord_guild_id = IntField()
    name = StringField()

    start_date = DateTimeField()
    end_date = DateTimeField()
    # duration = DateTimeField()

    # list of role ids
    role_restriction = ListField(StringField())
    participants = ListField(IntField())

    # multiple rewards possible
    rewards = ListField(IntField())

    def __init__(self, discord_guild_id=None, name="Custom Event", start_date=datetime.now(),
                 end_date=datetime.now() + timedelta(days=7), role_restrictions=None, rewards=None, participants=None,
                 *args, **kwargs):
        super(Event, self).__init__(*args, **kwargs)
        self.discord_guild_id = discord_guild_id
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.role_restriction = role_restrictions.split()
        self.participants = participants
        self.rewards = [rewards]  # todo multiple items within list

    def __str__(self):
        return f'Event "{self.name}":\nstarts: {self.start_date} - ends: {self.end_date}\nparticipating roles: {self.role_restriction}\nreward: {self.rewards}'
