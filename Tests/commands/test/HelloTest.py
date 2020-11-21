import asyncio
import unittest
from unittest.mock import patch, MagicMock


from discord_mage.commands.test.Hello import Hello

class AsyncMock(MagicMock):
    async def __call__(self, *args, **kwargs):
        return Hello.action(self, "test")

class TestHello(unittest.TestCase):

    @patch('discord_mage.commands.test.Hello.Hello.call', new_callable=AsyncMock)
    def test_call(self, test_hello):
        loop = asyncio.get_event_loop()
        result = loop.run_until_complete(Hello.call(None,"test"))
        self.assertEqual(result, "Hello! test")
        # test_hello.assert_called_with(self, "test")


if __name__ == '__main__':
    unittest.main()
