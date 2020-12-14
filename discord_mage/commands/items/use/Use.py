class Use:
    aliases = []
    brief = 'uses items'
    description = "uses items"

    @staticmethod
    async def call(context):
        return

    @staticmethod
    def action_invalid_argument(argument):
        return f"{argument} is an invalid argument"

    @staticmethod
    def action_set_argument(argument, value):
        return f"{argument} are now {value}"
