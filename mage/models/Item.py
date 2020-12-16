from mongoengine import Document, IntField, StringField, ListField, BooleanField, NotUniqueError


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

    # id = IntField()
    name = StringField(unique=True)
    cls_name = StringField(required=True)

    price = IntField(default=0, required=True)
    # category = ListField(StringField())
    brief = StringField()
    description = StringField()
    # is_enabled = BooleanField()
    # is_event_item = BooleanField()
    # is_shop_item = BooleanField()
    level_restriction = IntField(default=0)

    meta = {"allow_inheritance": True}

    def __init__(self, *args, **kwargs):
        super(Item, self).__init__(*args, **kwargs)

    def save_this(self, **kwargs):
        """ Updates this user

        :param kwargs: Query Operations
        :return: List with user
        """
        try:
            return Item.objects(
                name=self.name
            ).update_one(upsert=True, **kwargs)
        except NotUniqueError:
            raise NotUniqueError(f"Item already exists.")

    def __str__(self):
        return f"{self.name} {self.brief} Price: {self.price}"

