class OnReady:

    def call(self, client):
        print(self.action(client.user))

    def action(self, user):
        return f'Bot logged in as {user}'
