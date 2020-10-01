from mage.items.Steal import Steal
from mage.models.User import User


def test():
    user1 = User("Max", 100)
    user2 = User("Moritz", 100)

    Steal().action(user1, user2)

    if user1.points != 110:
        return "Test failed"

    if user2.points != 90:
        return "Test failed"

    print(user1)
    print(user2)
    return "Test success"




if __name__ == '__main__':
    result = test()
    print(result)
