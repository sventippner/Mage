class Ping:
    aliases = []
    brief = 'returns bot latency'
    description = 'Returns Bot latency in ms'

    @staticmethod
    async def call(self, context):
        """ this function is executed by a discord message """
        await context.send(Ping.action_latency(self.client.latency))

    @staticmethod
    def action_latency(latency):
        return f'latency: {round(latency * 1000)} ms'
