from utils.data_access import db_connect
from Tests.test_utils.FakeUser import get_fake_user


def main():
    db_connect()
    user = get_fake_user()
    print(user)

    user.save()


if __name__ == "__main__":
    main()