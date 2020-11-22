import asyncio
import unittest
from unittest.mock import patch, AsyncMock, MagicMock


from Tests.test_utils.FakeUser import get_fake_user
from Tests.test_utils.FakeServer import get_fake_server
from discord_mage.commands.points.Profile import Profile
from mage.models.Server import Server


class AsyncMock(MagicMock):

    server = get_fake_server()


    async def __call__(self, *args, **kwargs):
        user = get_fake_user()
        user.points = 3
        return Profile.action(AsyncMock.server, user)


class TestProfile(unittest.TestCase):

    server = get_fake_server()

    @patch('discord_mage.commands.points.Profile.Profile.call', new_callable=AsyncMock)
    def test_call(self, test_profile):
        loop = asyncio.get_event_loop()
        result = loop.run_until_complete(Profile.call(None))
        self.assertEqual(result, f"Level: **3**\n{TestProfile.server.points_name}: **3**\nPoints needed for Level-Up: 2")
        # test_test.assert_called_with(self, "test")

    def test_action(self):
        user = get_fake_user()
        user.points = 3333
        self.assertEqual(Profile.action(TestProfile.server, user),f"Level: **100** (MAX)\n{TestProfile.server.points_name}: **3333**")






if __name__ == '__main__':
    unittest.main()
