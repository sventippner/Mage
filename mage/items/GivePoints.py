from mage.models.Item import Item
from mage.models.User import User


class GivePoints(Item):
    name = "givepoints"
    cls_name = "GivePoints"
    aliases = ['item']
    brief = 'test item'
    description = 'asdasd'
    price = 20
    level_restriction = 0

    use_cost = 25

    def __init__(self, *args, **kwargs):
        super(Item, self).__init__(*args, **kwargs)

    @staticmethod
    def action(user: User, target: User, amount: int = 0):
        user.points -= amount + 25
        target.points += amount
        user.save()
        target.save()
