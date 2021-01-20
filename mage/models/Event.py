from mongoengine import Document, StringField, DateTimeField, IntField, ListField, EmbeddedDocumentListField, \
    NotUniqueError
from datetime import datetime, timedelta

from mage.models.ParticipatingRole import ParticipatingRole


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
    participating_roles = EmbeddedDocumentListField(ParticipatingRole)

    # multiple rewards possible
    rewards = ListField(StringField())

    def __init__(self, discord_guild_id=None, name="Custom Event", start_date=datetime.now(),
                 end_date=datetime.now() + timedelta(days=7), rewards=None, participating_roles=None,
                 *args, **kwargs):
        super(Event, self).__init__(*args, **kwargs)
        self.discord_guild_id = discord_guild_id
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.participating_roles = participating_roles
        self.rewards = rewards

    @staticmethod
    def find(**kwargs):
        return Event.objects(**kwargs)

    def delete_this(self):
        """ Deletes self document

        :return: Amount of deleted documents
        """
        return Event.objects(
            discord_guild_id=self.discord_guild_id,
            name=self.name,
            start_date=self.start_date,
            end_date=self.end_date,
            participating_roles=self.participating_roles,
            rewards=self.rewards
        ).delete()

    def save_this(self, *args, **kwargs):
        """ Updates this user

        :param kwargs: Query Operations
        :return: List with user
        """
        try:
            return Event.objects(
                discord_guild_id=self.discord_guild_id,
                name=self.name,
                start_date=self.start_date,
                end_date=self.end_date,
                participating_roles=self.participating_roles,
                rewards=self.rewards
            ).update_one(upsert=True, **kwargs)
        except NotUniqueError:
            raise NotUniqueError(f"Event already exists.")

    def __str__(self):
        return f'Event "{self.name}":\nstarts: {self.start_date} - ends: {self.end_date}\nreward: {self.rewards}\nRoles and corresponding participants: {self.participating_roles}'
