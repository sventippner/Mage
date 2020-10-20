from faker import Faker

from mage.models.User import User


def get_fake_user():
    fake = Faker()
    user = User()
    user.discord_user_id = str(fake.random.randint(1111111111, 9999999999))
    user.discord_guild_id = str(fake.random.randint(1111111111, 9999999999))
    user.points = fake.random.randint(0, 33000)
    user.pvp_status = fake.random.randint(0, 1)
    return user
