from discord_mage.commands.Hello import Hello


def test():
    param = "Martin"
    expected = "Hello! Martin"
    result = Hello().action(param)
    if result == expected:
        print("Test Hello success")
    else:
        print("Test Hello failed")


if __name__ == '__main__':
    test()
