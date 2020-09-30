class Hello:
    aliases = ['hallo', 'hi']
    brief = 'says hello'
    description = 'mentions user and says hello'

    async def call(self, context):
        await context.send(self.action(context.author.mention))

    def action(self, mention):
        return f"Hello! {mention}"
