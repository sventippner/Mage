from discord_mage.listeners.OnGuildJoin import OnGuildJoin
from discord_mage.tasks.ChangeStatus import ChangeStatus
from discord_mage.tasks.HandleServerEvents import HandleServerEvents
from mage.items.GivePoints import GivePoints
from mage.models.Item import Item
from utils import data_access, MagicTools
from mage.models.Server import Server


class OnReady:

    @staticmethod
    def call(client):
        OnReady.action_check_for_new_guilds(client)
        OnReady.action_start_tasks(client)

        OnReady.action_initialize_item_database(True)

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



    @staticmethod
    def action_initialize_item_database(force_init=False):
        print("Initializing item database")
        item_list = MagicTools.get_files_in_dir("/mage/items")

        for item_file in item_list:
            item = MagicTools.create_instance_of_item(item_file)
            if item:
                try:
                    if force_init or not data_access.find_one(Item, name=item.name):
                        print(f"add item {item.name}...", end=" ")
                        i = Item(
                            name=item.name,
                            price=item.price,
                            description=item.description,
                            brief=item.brief,
                            cls_name=item.cls_name,
                            # level_restriction=item.level_restriction
                        )
                        i.save_this(
                            name=item.name,
                            price=item.price,
                            description=item.description,
                            brief=item.brief,
                            cls_name=item.cls_name
                        )

                        print("success")
                except Exception:
                    print("failed")
        print("")
