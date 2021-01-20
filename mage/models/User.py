import discord
from mongoengine import StringField, Document, LongField, IntField, ListField, NotUniqueError, DictField

# from utils import data_access


class User(Document):
    """ User

    :param discord_user_id: Id of discord account
    :param discord_guild_id: Id of discord server
    :param points: amount of points the user with interactions and events
    :param items: list of items (item ids) the user has
    :param pvp_status: numeric flag of pvp status
    """
    discord_user_id = IntField()
    discord_guild_id = IntField()

    points = LongField(default=0)

    items = DictField(default={})

    pvp_status = IntField(default=0)
    health = IntField(default=100)

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

    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)
        self.name = ""

    @staticmethod
    def from_discord(discord_user_id, guild_id):
        u = User()
        u.discord_user_id = discord_user_id
        u.discord_guild_id = guild_id
        return u

    @staticmethod
    def find(**kwargs):
        return User.objects(**kwargs)

    def delete_this(self):
        """ Deletes self document

        :return: Amount of deleted documents
        """
        return User.objects(
            discord_user_id=self.discord_user_id,
            discord_guild_id=self.discord_guild_id
        ).delete()

    def save_this(self, *args, **kwargs):
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

    @property
    def level(self):
        """ Level System with points
        :return: level of user
        """

        current_points = self.points
        level = 1
        for i, needed_xp in enumerate(self.level_generator):
            if current_points >= needed_xp:
                level = i
            else:
                return level
        return level

    def has_item(self, item_name, *, amount=1):
        """ Checks if user has the item

        :param item_name: item id
        :return: Boolean
        """
        if str(item_name) in self.items.keys():
            if self.items[str(item_name)] >= amount:
                return True
        return False

    def obtain_item(self, item_name, *, amount=1):
        if str(item_name) in self.items.keys():
            self.items[str(item_name)] += amount
        else:
            self.items[str(item_name)] = amount

    def lose_item(self, item_name, *, amount=1):
        if str(item_name) in self.items.keys():
            if self.items[str(item_name)] >= amount + 1:
                self.items[str(item_name)] -= amount
            else:
                self.items.pop(str(item_name))

    def __str__(self):
        return f"User ID:{self.discord_user_id} ({self.points} Points) (Items: {self.items})"
