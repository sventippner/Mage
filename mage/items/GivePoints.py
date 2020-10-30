from mage.models.Item import Item
from mage.models.User import User


class GivePoints:
    aliases = ['item']
    brief = 'test item'
    description = ''

    use_cost = 25

    @staticmethod
    def action(user: User, target: User, amount: int = 0):
        user.points -= amount + 25
        target.points += amount
        user.save()
        target.save()

        # return f"{user.name} gibt {target.name} {amount} Punkte"  # Todo: change points name
