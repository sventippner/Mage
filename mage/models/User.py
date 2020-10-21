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

    max_level = 100
    # required points to reach level x is in level_generator[x]
    level_generator = [round((x ** 2) / 3) for x in range(max_level + 1)]
    level_generator[0] = 0  # ignore level 0
    level_generator[1] = 0  # default level users start with, 0 XP needed

    def __init__(self, points=0, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)
        self.points = points

    def save(self, *args, **kwargs):
        """ Updates this user

        :param kwargs: Query Operations
        :return: List with user
        """
        try:
            return User.objects(
                discord_user_id=self.discord_user_id,
                discord_guild_id=self.discord_guild_id
            ).update_one(upsert=True, **kwargs)
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

    @property
    def level(self):
        """ Level System with points
        :return: level of user
        """

        current_points = self.points    # TODO update current points if needed??
        level = 1
        for i, needed_xp in enumerate(self.level_generator):
            if current_points >= needed_xp:
                level = i
            else:
                return level

    def __str__(self):
        return f"User ID:{self.discord_user_id} ({self.points} Points)"
