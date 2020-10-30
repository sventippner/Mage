from mongoengine import Document, IntField, EmbeddedDocument, StringField, NotUniqueError


class Reaction(EmbeddedDocument):
    emoji = StringField(required=True)
    role = StringField(required=True)

    def __init__(self, emoji, role, *args, **kwargs):
        super(Reaction, self).__init__(*args, **kwargs)
        self.emoji = emoji
        self.role = role


    def save_this(self, *args, **kwargs):
        """ Updates this Reaction

        :param kwargs: Query Operations
        :return: List with user
        """
        try:
            return Reaction.objects(
                emoji=self.emoji,
                role=self.role
            ).update_one(upsert=True, **kwargs)
        except NotUniqueError:
            raise NotUniqueError(f"Reaction already exists.")


    def delete_this(self):
        """ Deletes self document

        :return: Amount of deleted documents
        """
        return Reaction.objects(
            emoji=self.emoji,
            role=self.role
        ).delete()
