class Hello:

    aliases = ['hallo', 'hi']
    brief = 'says hello'
    description = 'mentions user and says hello'

    async def call(self, context):
        await context.send(f'Hello! {context.author.mention}')
