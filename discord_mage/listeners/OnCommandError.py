from discord.ext import commands
from config import DEFAULT_PREFIX


class OnCommandError:

    @staticmethod
    async def call(context, error):
        mention = context.message.author.mention

        if isinstance(error, commands.CommandNotFound):
            await context.send(OnCommandError.action_command_not_found(mention))
        # elif isinstance(error, commands.MissingRequiredArgument):
        #     await context.send(OnCommandError.action_missing_required_argument(mention))
        # elif isinstance(error, commands.MissingPermissions):
        #     await context.send(OnCommandError.action_missing_permissions(mention))
        # elif isinstance(error, commands.CheckFailure):
        #     await context.send(OnCommandError.action_check_failure(mention))
        # elif isinstance(error, commands.BadArgument):
        #     await context.send(OnCommandError.action_is_bad_argument(mention))
        # elif isinstance(error, commands.CommandInvokeError):
        #     await context.send(OnCommandError.action_command_invoke_error(mention))
        # elif isinstance(error, commands.ExpectedClosingQuoteError) or isinstance(error, commands.UnexpectedQuoteError):
        #     await context.send(OnCommandError.action_quote_error(mention))
        else:
            # raise all other errors
            OnCommandError.action_raise_error(error)

    @staticmethod
    def action_command_not_found(mention=""):
        return f"{mention} Command not found. Check `{DEFAULT_PREFIX}help` for information."

    @staticmethod
    def action_missing_required_argument(mention=""):
        return f"{mention} Missing required argument(s). Check `{DEFAULT_PREFIX}help` for information."

    @staticmethod
    def action_missing_permissions(mention=""):
        return f"{mention} You are missing permissions to use this command."

    @staticmethod
    def action_is_bad_argument(mention=""):
        return f"{mention} You have used wrong argument(s). Check `{DEFAULT_PREFIX}help` for information."

    @staticmethod
    def action_command_invoke_error(mention=""):
        return f"{mention} An error occured while executing the command.\nThis is probably caused due to an incorrect use of the command.\nCheck `{DEFAULT_PREFIX}help` for information."

    @staticmethod
    def action_quote_error(mention=""):
        return f"{mention} Found unexpected quotes while parsing the command arguments."

    @staticmethod
    def action_check_failure(mention=""):
        return "{mention} Command can not be executed. Checks failed"

    @staticmethod
    def action_raise_error(error):
        raise error



