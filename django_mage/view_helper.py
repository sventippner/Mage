from mage.models.Server import Server
from utils import data_access


def get_server_list():
    server_list = data_access.find(Server)
    return server_list

def get_server_data(id:str):
    server_data = data_access.find_one(Server, discord_guild_id=id)
    return server_data
