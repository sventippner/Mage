from mongoengine import Document, IntField, StringField, ListField, BooleanField, NotUniqueError
import utils.data_access as data
from mage.models.User import User


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

    name = StringField(unique=True)
    item_file = StringField(required=True)

    price = IntField(default=0, required=True)
    use_cost = IntField()
    categories = ListField(StringField())
    brief = StringField()
    description = StringField()
    is_consumable = BooleanField()
    is_enabled = BooleanField()
    is_event_item = BooleanField()
    is_shop_item = BooleanField()
    level_restriction = IntField(default=0)

    meta = {"allow_inheritance": True}

    @staticmethod
    def append_categories(categories, is_consumable, is_event_item, level_restriction):
        if is_consumable:
            categories.append("Consumables")
        if is_event_item:
            categories.append("Event Items")
        if level_restriction > 1:
            categories.append("Level Restricted")

    @staticmethod
    def on_buy(*args, **kwargs):
        pass

    @classmethod
    def on_use(cls, *args, **kwargs):
        pass

    @classmethod
    def pre_use(cls, user):
        ok = cls.check_permissions(user)
        if ok:
            return True
        else:
            return False

    @classmethod
    def check_permissions(cls, user: User):
        if \
        (
            cls.is_enabled and
            user.points >= cls.use_cost and
            user.level >= cls.level_restriction and
            user.has_item(cls.id)
        ):
            return True
        return False

    @classmethod
    def pay_use_cost(cls, user: User):
        user.points -= cls.use_cost

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
