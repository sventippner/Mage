import asyncio
import unittest
from unittest.mock import patch, AsyncMock, MagicMock

from discord_mage.commands.events.StartEvent import StartEvent
from mage.models.Event import Event


class TestStartEvent(unittest.TestCase):

    @patch('discord_mage.commands.events.StartEvent.StartEvent.call')
    def test_call(self, test_event):
        event = Event()
        loop = asyncio.get_event_loop()
        result = loop.run_until_complete(StartEvent.call(None,event.name, event.start_date, event.end_date, event.rewards, event.participating_roles))
        test_event.assert_called_with(None,event.name, event.start_date, event.end_date, event.rewards, event.participating_roles)




if __name__ == '__main__':
    unittest.main()
