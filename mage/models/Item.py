from mongoengine import Document, IntField, StringField, ListField, BooleanField


class Item(Document):
    """ Item

    :param id
    :param name: Name
    :param price: Price
    :param category: Category
    :param brief: The short help text.
    :param description: Description of the item.
    :param is_event_item: boolean
    :param is_shop_item: boolean
    """

    id = IntField()
    name = StringField(unique=True)

    price = IntField()
    category = ListField(StringField())
    brief = StringField()
    description = StringField()
    is_enabled = BooleanField()
    is_event_item = BooleanField()
    is_shop_item = BooleanField()
    level_restriction = IntField()

    meta = {"allow_inheritance": True}

    def __str__(self):
        return f"{self.name} {self.brief} Price: {self.price}"