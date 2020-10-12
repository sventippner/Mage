import unittest


class TemplateTests(unittest.TestCase):
    """ template test
    doc: https://docs.python.org/3/library/unittest.html#unittest.TestCase.debug
    """

    @classmethod
    def setUpClass(cls):
        """ setUpClass is called before setup(), but only once. """
        print("setUpClass()")

    def setUp(self):
        """ setUp is called before every test. """
        print("setUp()")

    @classmethod
    def tearDownClass(cls):
        """ tearDownClass is called once after all tests are done. """
        print("tearDownClass()")

    def test_example_1(self):
        print("test_example_1()")

    def test_example_2(self):
        print("test_example_2()")


if __name__ == '__main__':
    unittest.main()
