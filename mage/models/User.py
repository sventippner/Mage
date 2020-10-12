from mongoengine import StringField, Document, LongField, IntField, ListField, NotUniqueError

from utils import data_access


class User(Document):
    """ User

    :param discord_user_id: Id of discord account
    :param discord_guild_id: Id of discord server
    :param points: amount of points the user with interactions and events
    :param items: list of items (item ids) the user has
    :param pvp_status: numeric flag of pvp status
    """
    discord_user_id = StringField(regex=r"\d")
    discord_guild_id = StringField(regex=r"\d")
    points = LongField()
    items = ListField(IntField())
    pvp_status = IntField()

    meta = {
        'indexes': [
            {'fields': ('discord_user_id', 'discord_guild_id'), 'unique': True}
        ]
    }

    def __init__(self, points=0, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)
        self.points = points

    def save(self, *args, **kwargs):
        try:
            super().save(*args, **kwargs)
            return True
        except NotUniqueError:
            raise NotUniqueError(f"User already exists.")
            return False

    def find(self, **kwargs):
        return self.objects(**kwargs)

    def delete_this(self):
        """ Deletes self document

        :return: Amount of deleted documents
        """
        return User.objects(
            discord_user_id=self.discord_user_id,
            discord_guild_id=self.discord_guild_id
        ).delete()

    def update(self, **kwargs):
        return User.objects(
            discord_user_id=self.discord_user_id,
            discord_guild_id=self.discord_guild_id
        ).update(**kwargs)

    def __str__(self):
        return f"User ID:{self.discord_user_id} ({self.points} Points)"
