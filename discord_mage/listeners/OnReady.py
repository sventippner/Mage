from discord_mage.listeners.OnGuildJoin import OnGuildJoin
from utils import data_access
from mage.models.Server import Server

class OnReady:

    @staticmethod
    def call(client):
        OnReady.action_check_for_new_guilds(client)
        print(OnReady.action_login(client.user))

    @staticmethod
    def action_check_for_new_guilds(client):
        for guild in client.guilds:
            server = data_access.find_one(Server, discord_guild_id=guild.id)
            if not server:
                server = Server(guild)
                OnGuildJoin.action_save_server(server)

    @staticmethod
    def action_login(user):
        return f'Bot logged in as {user}'
