from mage.models.Item import Item
from mage.models.User import User


class GivePoints(Item):
    __metaclass__ = Item

    name = "givepoints"
    aliases = ['item']
    brief = 'test item'
    description = ''
    price = 20

    use_cost = 25

    def __init__(self, *args, **kwargs):
        super(Item, self).__init__(*args, **kwargs)

    @staticmethod
    def action(user: User, target: User, amount: int = 0):
        user.points -= amount + 25
        target.points += amount
        user.save()
        target.save()
