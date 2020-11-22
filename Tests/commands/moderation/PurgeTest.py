import asyncio
import unittest
from unittest.mock import patch, MagicMock

from discord_mage.commands.moderation.Purge import Purge


class TestPurge(unittest.TestCase):

    @patch('discord_mage.commands.moderation.Purge.Purge.call')
    def test_call(self, test_purge):
        loop = asyncio.get_event_loop()
        result = loop.run_until_complete(Purge.call(None,3))
        # self.assertEqual(result, "Hello! test")
        test_purge.assert_called_with(None, 3)



if __name__ == '__main__':
    unittest.main()

