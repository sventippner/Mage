from mongoengine import Document, StringField, ListField


class SimpleDiscordCommand(Document):
    name = StringField(max_length=30, unique=True)
    aliases = ListField(StringField())
    brief = StringField(max_length=100)
    description = StringField(max_length=200)

    output = StringField()

    def __str__(self):
        return f'{self.name}'
