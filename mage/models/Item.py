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
    is_event_item = BooleanField()
    is_shop_item = BooleanField()
    level_restriction = IntField()


    """
    action = StringField()

    def action(self):
        try:
            method_to_call = getattr(items, self.action)
            result = method_to_call()
            return result
        except Exception:
            raise ItemError(f"Could not execute {self.name}.action()")
    """
