from discord_mage.listeners.OnGuildJoin import OnGuildJoin
from discord_mage.tasks.ChangeStatus import ChangeStatus
from discord_mage.tasks.HandleServerEvents import HandleServerEvents
from mage.items.GivePoints import GivePoints
from utils import data_access
from mage.models.Server import Server


class OnReady:

    @staticmethod
    def call(client):
        OnReady.action_check_for_new_guilds(client)
        OnReady.action_start_tasks(client)

        # OnReady.action_initialize_item_database()

        print(OnReady.action_login(client.user))

    @staticmethod
    def action_check_for_new_guilds(client):
        for guild in client.guilds:
            server = data_access.find_one(Server, discord_guild_id=guild.id)
            if not server:
                server = Server(guild)
                OnGuildJoin.action_save_server(server)

    @staticmethod
    def action_start_tasks(client):
        ChangeStatus(client).call.start()
        HandleServerEvents(client).call.start()

    @staticmethod
    def action_login(user):
        return f'Bot logged in as {user}'


    # Todo: not working
    # Todo: Write items in database on bot start
    @staticmethod
    def action_initialize_item_database():
        itemlist = [GivePoints()]

        for i in itemlist:
            print(i)
            i.save()