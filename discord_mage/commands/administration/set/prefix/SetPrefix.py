from mage.models.Server import Server
from utils import data_access


class SetPrefix:
    aliases = []
    brief = 'changes bot prefix'
    description = 'changes command prefix on this server for all users'

    @staticmethod
    async def call(context, prefix):
        """ this function is executed by a discord message """
        if SetPrefix.action_is_valid(prefix):
            guild = data_access.find_one(Server, discord_guild_id=context.guild.id)
            guild.bot_prefix = prefix
            guild.save()
            await context.send(SetPrefix.action_changed_prefix(context))
        else:
            await context.send(SetPrefix.action_not_valid(prefix))

    @staticmethod
    def action_changed_prefix(context):
        return f'Prefix has been changed to **{data_access.get_prefix(context.guild.id)}**'

    @staticmethod
    def action_is_valid(prefix: str):
        return prefix.isascii() and prefix.isprintable() and '"' not in prefix and "'" not in prefix and 1 <= len(prefix) <= 5

    @staticmethod
    def action_not_valid(invalid_prefix):
        return f'Prefix has not been changed.\n{invalid_prefix} is not a valid prefix.'
