class Hello:
    aliases = ['hallo', 'hi']
    brief = 'says hello'
    description = 'mentions user and says hello'

    async def discord_call(self, context):
        """ this function is executed by a discord message """
        await context.send(self.action(context.author.mention))

    def action(self, mention):
        return f"Hello! {mention}"
