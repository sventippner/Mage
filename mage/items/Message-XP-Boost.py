from mongoengine import IntField, ReferenceField
import discord

from discord_mage.listeners import OnMessage
from mage.models.Item import Item
from mage.models.User import User
from random import randint
import utils.data_access as data


class MessageXPBoost(Item):
    # overriden attributes
    name = "Meassage-XP-Boost"
    brief = 'receive a One-Week Message-XP-Boost'
    description = 'it multiplies your gained XP by 2'
    price = 5000
    use_cost = 0
    level_restriction = 0

    categories = ["Boost"]
    is_consumable = True
    is_enabled = True
    is_event_item = True
    is_shop_item = True

    Item.append_categories(categories, is_consumable, level_restriction)

    def __init__(self, *args, **kwargs):
        super(Item, self).__init__(*args, **kwargs)

    @staticmethod
    def on_buy(context):
        pass

    @classmethod
    async def on_use(cls, context, name):
        user = data.find_one(User, discord_user_id=context.author.id, discord_guild_id=context.guild.id)
        user.name = context.author.display_name
        guild = context.guild

        OnMessage.OnMessage.points_per_message *= 2




    @staticmethod
    async def action_is_ok(user, context):
        pass


    @staticmethod
    def action_success(context, user):
        return f"{context.author.display_name} started an private XP-Boost. Ends {OneWeeklater}"

    @staticmethod
    def action_is_not_ok(guild):
        return f"You do not have enough {guild.points_name}! You need at least {MessageXPBoost.use_cost}"
