from mongoengine import Document, IntField, StringField, ListField

from mage import items
from mage.Exceptions import ItemError

# todo: Category
# todo: id
# todo: command


class Item(Document):
    """ Item

    :param id
    :param name: Name
    :param price: Price
    :param category: Category
    :param brief: The short help text.
    :param description: Description of the item.
    :param action: item function
    """

    id = IntField()
    name = StringField()

    price = IntField()
    category = ListField(StringField())
    brief = StringField()
    description = StringField()

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