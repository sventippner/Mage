from discord.ext import commands


class OnCommandError:

    @staticmethod
    async def call(context, error):
        if isinstance(error, commands.CommandNotFound):
            await context.send(await OnCommandError.action_command_not_found())
        elif isinstance(error, commands.MissingRequiredArgument):
            await context.send(await OnCommandError.action_missing_required_argument())
        elif isinstance(error, commands.MissingPermissions):
            await context.send(await OnCommandError.action_missing_permissions())
        elif isinstance(error, commands.CheckFailure):
            await context.send(await OnCommandError.action_is_guild_command())
        else:
            # raise all other errors
            OnCommandError.action_raise_error(error)

    @staticmethod
    async def action_command_not_found():
        return "command not found"

    @staticmethod
    async def action_missing_required_argument():
        return "Missing required argument(s)"

    @staticmethod
    async def action_missing_permissions():
        return "You are missing permissions to use this command."

    @staticmethod
    async def action_is_guild_command():
        return "Command is supposed to be used in a server"

    @staticmethod
    def action_raise_error(error):
        raise error
