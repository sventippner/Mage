from utils.Secrets import Secrets


class IsBotOwner:

    @staticmethod
    def is_bot_owner(ctx):
        """
        returns True if user is a bot developer
        :param ctx: context object
        :return: bool
        """
        owners = Secrets().get("BOT_OWNERS").split(", ")
        return str(ctx.author.id) in owners
