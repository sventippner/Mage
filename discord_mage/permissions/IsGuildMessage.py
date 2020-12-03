class IsGuildMessage:

    @staticmethod
    def is_guild_message(ctx):
        """
        returns True if user is a bot developer
        :param ctx: context object
        :return: bool
        """
        if ctx.guild:
            return True
        return False
