from mongoengine import Document, IntField, StringField, ListField, BooleanField


class Item(Document):
    """ Item

    :param id
    :param name: Name
    :param price: Price
    :param categories: Category
    :param brief: The short help text.
    :param description: Description of the item.
    :param is_consumable: boolean, item will be deleted upon use
    :param is_event_item: boolean, can be an event reward
    :param is_shop_item: boolean, is listed in shop
    """

    id = IntField()
    name = StringField(unique=True)

    price = IntField()
    use_cost = IntField()
    categories = ListField(StringField())
    brief = StringField()
    description = StringField()
    is_consumable = BooleanField()
    is_enabled = BooleanField()
    is_event_item = BooleanField()
    is_shop_item = BooleanField()
    level_restriction = IntField()

    meta = {"allow_inheritance": True}

    @staticmethod
    def append_categories(categories, is_consumable, is_event_item, level_restriction):
        if is_consumable:
            print("cls.is_consumable")
            categories.append("Consumables")
        if is_event_item:
            print("cls.is_event_item")
            categories.append("Event Items")
        if level_restriction > 1:
            print("cls.level_restriction")
            categories.append("Level Restricted")

    @staticmethod
    def on_buy(*args, **kwargs):
        pass

    @staticmethod
    def on_use(*args, **kwargs):
        pass

    @staticmethod
    def action_insufficient_points_to_use():
        return "You have insufficient Points to use this Item"

    def __str__(self):
        return f"{self.name} {self.brief} Price: {self.price}"
