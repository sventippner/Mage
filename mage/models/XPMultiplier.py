import datetime

from mongoengine import Document, IntField, DateTimeField, NotUniqueError


class XPMultiplier(Document):
    discord_user_id = IntField(required=True)
    discord_guild_id = IntField(required=True)
    multiplier = IntField(required=True, default=2)
    end_date = DateTimeField(required=True, default=(datetime.datetime.today() + datetime.timedelta(days=7)))

    def __init__(self, *args, **kwargs):
        super(XPMultiplier, self).__init__(*args, **kwargs)

    def save_this(self, **kwargs):
        """ Updates this user

        :param kwargs: Query Operations
        :return: List with user
        """
        try:
            return XPMultiplier.objects(
                discord_user_id=self.discord_user_id,
                discord_server_id=self.discord_guild_id,
            ).update_one(upsert=True, **kwargs)
        except NotUniqueError:
            raise NotUniqueError(f"XPMultiplier already exists.")

    def delete_this(self):
        """ Deletes self document

        :return: Amount of deleted documents
        """
        return XPMultiplier.objects(
            discord_user_id=self.discord_user_id,
            discord_guild_id=self.discord_guild_id
        ).delete()
