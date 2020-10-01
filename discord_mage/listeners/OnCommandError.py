from discord.ext import commands


class OnCommandError:

    async def call(self, context, error):
        if isinstance(error, commands.CommandNotFound):
            await context.send(self.action_command_not_found())
        elif isinstance(error, commands.MissingRequiredArgument):
            await context.send(self.action_missing_required_argument())
        elif isinstance(error, commands.MissingPermissions):
            await context.send(self.action_missing_permissions())
        else:
            # raise all other errors
            self.action_raise_error(error)

    async def action_command_not_found(self):
        return "command not found"

    async def action_missing_required_argument(self):
        return "Missing required argument(s)"

    async def action_missing_permissions(self):
        return "You are missing permissions to use this command."

    def action_raise_error(self, error):
        raise error
