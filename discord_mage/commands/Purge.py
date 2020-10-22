class Purge:
    aliases = []
    brief = 'deletes messages'
    description = 'deletes the last [amount] messages in the channel. Default value for amount is 2'

    @staticmethod
    async def call(context, amount=2):
        """ this function is executed by a discord message """
        if 0 < amount <= 50:
            await context.channel.purge(limit=amount)
        else:
            await context.send(f'{amount} is not a viable amount. You can only purge 1 to 50 messages')
