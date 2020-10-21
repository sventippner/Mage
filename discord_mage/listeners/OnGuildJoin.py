from utils import data_access
from mage.models.Server import Server


class OnGuildJoin:

    @staticmethod
    def call(guild):
        server = data_access.find(Server, discord_guild_id=guild.id)
        if not server:
            server = Server(guild)
            OnGuildJoin.action_save_server(server)

    @staticmethod
    def action_save_server(server):
        server.save()
