from mage.models.Item import Item


class Steal(Item):
    """ Steals Points from a user. """

    steal_amount = 10

    def __init__(self):
        Item.__init__(self, "Steal")

    def action(self, user, target, steal_increase=0):
        """ User steals points from the target.

        :param user: gains points
        :param target: loses points
        :param steal_increase: adds to the base steal amount
        """
        target.points -= self.steal_amount + steal_increase
        user.points += self.steal_amount + steal_increase
