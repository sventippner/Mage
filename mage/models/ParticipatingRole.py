from mongoengine import IntField, EmbeddedDocument, NotUniqueError, ListField


class ParticipatingRole(EmbeddedDocument):
    role_id = IntField(required=True)
    discord_user_ids = ListField(IntField())
    points = IntField(default=0)

    def __init__(self, role_id, discord_user_ids, points, *args, **kwargs):
        super(ParticipatingRole, self).__init__(*args, **kwargs)
        self.role_id = role_id
        self.discord_user_ids = discord_user_ids
        self.points = points


    def save_this(self, *args, **kwargs):
        """ Updates this Reaction

        :param kwargs: Query Operations
        :return: List with user
        """
        try:
            return ParticipatingRole.objects(
                role_id=self.role_id,
                discord_user_ids=self.discord_user_ids,
                points=self.points
            ).update_one(upsert=True, **kwargs)
        except NotUniqueError:
            raise NotUniqueError(f"Participating Role already exists.")


    def delete_this(self):
        """ Deletes self document

        :return: Amount of deleted documents
        """
        return ParticipatingRole.objects(
            role_id=self.role_id,
            discord_user_ids=self.discord_user_ids,
            points=self.points
        ).delete()

    def __str__(self):
        return f"(RoleID: {self.role_id}, Points: {self.points}, UserIDs: {self.discord_user_ids})"