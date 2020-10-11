from mongoengine import Document, IntField, StringField, ListField


# todo: Category
# todo: id
# todo: command

class Item(Document):
    """ Item

    :param name: Name
    :param price: Price
    :param category: Category
    :param brief_description: The short help text.
    :param long_description: Description of the item.
    """

    name = StringField()
    price = IntField()
    category = ListField(StringField())
    brief_description = StringField()
    long_description = StringField()
