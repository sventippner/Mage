"""

    @commands.command(brief="buys item from shop",
                      description=f"buys item from shop with the corresponding ID. Use {DEFAULT_PREFIX}shop to list all available items. Example: {DEFAULT_PREFIX}buyitem 1")
    async def buyitem(self, context, i: int):

        buys item with corresponding id :i:
        :param context: context object automatically passed on function call
        :param i: item id (also corresponds to item id in database)


        if not database.has_item(context.author.id, context.guild.id, i):
            points = database.get_points(context.author.id, context.guild.id)
            price = database.get_price_from_item(i)
            if points >= price:
                database.add_item(context.author.id, context.guild.id, i)
                database.add_participation_points(db, context.author.id, context.guild.id, -price)
                points = database.get_points(context.author.id, context.guild.id)
                database.adjust_level(context.author.id, context.guild.id)
                await context.send(f"You bought item {database.get_item_name_by_id(i)}\nNew Balance: **{points}** points.")
            else:
                await context.send(f"Insufficient points. You only have **{points}** points.")
        else:
            await context.send("You already own this item")

"""
from mage.models.Item import Item
from mage.models.Server import Server
from utils import data_access
from utils.MagicTools import get_item_list


class BuyItem:
    aliases = []
    brief = 'buys item from shop'
    description = "buys item from shop with the corresponding ID. " \
                  "Use {DEFAULT_PREFIX}shop to list all availableitems. " \
                  "Example: {DEFAULT_PREFIX}buyitem 1 "

    @staticmethod
    async def call(context, item_name):
        """ this function is executed by a discord message """
        # item = data_access.find_one(Item, name=item_name)

        if item_name in get_item_list():
            user = data_access.find_user_by_discord_message(context.message)
            server = data_access.find_one(Server, discord_guild_id=context.guild.id)
            result = BuyItem.action_buy_item(server, user, item)

        await context.send(result)


    @staticmethod
    def action_buy_item(server, user, item):
        if not item:
            return f"Item not found."
        if user.points <= item.price:
            return f"Not sufficient {server.points_name} to buy {item.name}"
        else:
            user.items.append(item.name)
            user.points -= item.price
            user.save_this()
            return f"{item.name} bought."
