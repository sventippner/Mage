import discord


class IsDirectMessage:

    @staticmethod
    def is_direct_message(ctx):
        """
        returns True if user is a bot developer
        :param ctx: context object
        :return: bool
        """
        if isinstance(ctx.channel, discord.channel.DMChannel):
            return True
        return False
