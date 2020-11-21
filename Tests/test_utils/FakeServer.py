from mage.models.Server import Server

def get_fake_server():
    server = Server()
    server.points_name = "Points"
    return server