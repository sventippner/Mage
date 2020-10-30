from mongoengine import Document, IntField, EmbeddedDocumentListField, NotUniqueError

from mage.models.Reaction import Reaction


class Message(Document):
    discord_message_id = IntField()
    discord_guild_id = IntField(required=True)
    reactions = EmbeddedDocumentListField(Reaction)

    def __init__(self, discord_message_id=None, discord_guild_id=None, reactions=[], *args, **kwargs):
        super(Message, self).__init__(*args, **kwargs)
        self.discord_message_id = discord_message_id
        self.discord_guild_id = discord_guild_id
        self.reactions = reactions


    def save_this(self, *args, **kwargs):
        """ Updates this user

        :param kwargs: Query Operations
        :return: List with user
        """
        try:
            return Message.objects(
                discord_message_id=self.discord_message_id
            ).update_one(upsert=True, **kwargs)
        except NotUniqueError:
            raise NotUniqueError(f"User already exists.")


    def delete_this(self):
        """ Deletes self document

        :return: Amount of deleted documents
        """
        return Message.objects(
            discord_message_id=self.discord_message_id
        ).delete()
