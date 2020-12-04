from discord.ext import commands
from config import DEFAULT_PREFIX


class OnCommandError:

    @staticmethod
    async def call(context, error):
        if isinstance(error, commands.CommandNotFound):
            await context.send(OnCommandError.action_command_not_found())
        elif isinstance(error, commands.MissingRequiredArgument):
            await context.send(OnCommandError.action_missing_required_argument())
        elif isinstance(error, commands.MissingPermissions):
            await context.send(OnCommandError.action_missing_permissions())
        elif isinstance(error, commands.CheckFailure):
            await context.send(OnCommandError.action_is_guild_command())
        elif isinstance(error, commands.BadArgument):
            await context.send(OnCommandError.action_is_bad_argument())
        elif isinstance(error, commands.CommandInvokeError):
            await context.send(OnCommandError.action_command_invoke_error())
        elif isinstance(error, commands.ExpectedClosingQuoteError) or isinstance(error, commands.UnexpectedQuoteError):
            await context.send(OnCommandError.action_quote_error())
        else:
            # raise all other errors
            OnCommandError.action_raise_error(error)

    @staticmethod
    def action_command_not_found():
        return f"Command not found. Check `{DEFAULT_PREFIX}help` for information."

    @staticmethod
    def action_missing_required_argument():
        return f"Missing required argument(s). Check `{DEFAULT_PREFIX}help` for information."

    @staticmethod
    def action_missing_permissions():
        return "You are missing permissions to use this command."

    @staticmethod
    def action_is_guild_command():
        return "Command is supposed to be used in a server"

    @staticmethod
    def action_is_bad_argument():
        return f"You have used wrong argument(s). Check `{DEFAULT_PREFIX}help` for information."

    @staticmethod
    def action_command_invoke_error():
        return f"An error occured while executing the command.\nThis is probably caused due to an incorrect use of the command.\nCheck `{DEFAULT_PREFIX}help` for information."

    @staticmethod
    def action_quote_error():
        return "Found unexpected quotes while parsing the command arguments."

    @staticmethod
    def action_raise_error(error):
        raise error



