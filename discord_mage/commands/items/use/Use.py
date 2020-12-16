from mage.models.Server import Server
from utils import data_access, MagicTools


class Use:
    aliases = []
    brief = 'uses items'
    description = "uses items"

    @staticmethod
    async def call(context, item_name):
        if not item_name:
            await context.send("item not found.")
        else:
            user = data_access.find_user_by_discord_message(context.message)
            server = data_access.find_one(Server, discord_guild_id=context.guild.id)
            msg = Use.action_use_item(server, user, item_name)

            await context.send(msg)

    @staticmethod
    def action_use_item(server, user, item_name):
        if item_name in user.items:
            item = MagicTools.create_instance_of_item(item_name)
            return f"{item.name} used."
        else:
            return "You don't have this item."
