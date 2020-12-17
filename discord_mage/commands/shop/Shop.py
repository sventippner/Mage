"""
    async def shop(self, context):

        shows all items available for purchase
        :param context: context object automatically passed on function call

        items = database.get_all_items()
        msg = "Use the command `buyitem <id>` to buy an item from the shop."
        for item in items:
            i, name, price, description, level_restriction = item
            msg += f'\n\n**{i}. {name}\tprice: {price}**\nRequired level to use: {level_restriction}\n*{description}*'
        await context.send(msg)

"""
from pprint import pprint

from mage.models.Item import Item
from utils import data_access, MagicTools


class Shop:
    aliases = []
    brief = 'opens shop'
    description = "shows all items available for purchase"

    @staticmethod
    async def call(context):
        msg = Shop.action_list_shop_items()
        await context.send(msg)

    @staticmethod
    def action_list_shop_items():
        # items = data_access.find(Item, is_shop_item=True)
        items = data_access.find(Item)

        if not items:
            return "Our shop is sold out."

        msg = "Use the command `buyitem <id>` to buy an item from the shop."
        for i in items:
            try:
                item_obj = MagicTools.create_instance_of_item(i.item_file)
                msg += f'\n\n**{item_obj.name}\tprice: {item_obj.price}**\nRequired level to use: <todo: level_restriction> \n{item_obj.description}'
            except Exception:
                pass

        return msg
