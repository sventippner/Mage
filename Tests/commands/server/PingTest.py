import asyncio
import unittest
from unittest.mock import patch,  MagicMock

from discord_mage.commands.server.Ping import Ping


class AsyncMock(MagicMock):
    async def __call__(self, *args, **kwargs):
        return Ping.action_latency(0.2)

class TestPing(unittest.TestCase):

    @patch('discord_mage.commands.server.Ping.Ping.call', new_callable=AsyncMock)
    def test_call(self, test_ping):
        loop = asyncio.get_event_loop()
        result = loop.run_until_complete(Ping.call(None,"test"))
        self.assertEqual(result, "latency: 200 ms")
        # test_test.assert_called_with(self, "test")



if __name__ == '__main__':
    unittest.main()
