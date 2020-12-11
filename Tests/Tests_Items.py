import unittest

# from mage.items import *
from discord_mage.commands.shop.Shop import Shop
from utils.Secrets import Secrets
from utils.data_access import db_connect


class TemplateTests(unittest.TestCase):
    """ template test
    doc: https://docs.python.org/3/library/unittest.html#unittest.TestCase.debug
    """

    @classmethod
    def setUpClass(cls):
        """ setUpClass is called before setup(), but only once. """
        DISCORD_TOKEN = Secrets().get("DISCORD_TOKEN")

        db_connect()

        #print("setUpClass()")

    def setUp(self):
        """ setUp is called before every test. """
        #print("setUp()")

    @classmethod
    def tearDownClass(cls):
        """ tearDownClass is called once after all tests are done. """
        #print("tearDownClass()")

    def test_shop(self):
        print("Test shop()")

        msg = Shop.action_list_shop_items()
        print(msg)


if __name__ == '__main__':
    unittest.main()
