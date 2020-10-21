from mage.models.Server import Server


class OnGuildRemove:

    @staticmethod
    def call(guild):
        OnGuildRemove.action_delete_server(Server(guild))

    @staticmethod
    def action_delete_server(server):
        server.delete_this()
