from mongoengine import IntField, ReferenceField
import discord

from mage.models.Item import Item
from mage.models.User import User
from random import randint
import utils.data_access as data


class Dice(Item):
    # overriden attributes
    name = "Dice"
    brief = 'role a dice'
    description = 'role a dice and gain or loose points'
    price = 500
    use_cost = 60
    level_restriction = 0

    categories = ["Gamble"]
    is_consumable = False
    is_enabled = True
    is_event_item = False
    is_shop_item = True

    Item.append_categories(categories, is_consumable, is_event_item, level_restriction)

    def __init__(self, *args, **kwargs):
        super(Item, self).__init__(*args, **kwargs)

    @staticmethod
    def on_buy():
        pass

    @classmethod
    async def on_use(cls, context):
        user = data.find_one(User, discord_user_id=context.author.id, discord_guild_id=context.guild.id)
        user.name = context.author.display_name
        guild = context.guild

        if user.points - Dice.use_cost < 0:
            Dice.action_is_not_ok(guild)
        else:
            await Dice.action_is_ok(user, context)


    @staticmethod
    async def action_is_ok(user, context):
        amount = 0

        role_result = randint(1, 6)
        if role_result == 6:
            amount = 100
        if 4 < role_result < 6:
            amount = 40
        if role_result < 4:
            amount = 0

        user.points = user.points + amount - Dice.use_cost
        user.save()
        msg = Dice.action_success(context, user, role_result)
        await context.send(msg)

    @staticmethod
    def action_success(context, user, role_result):
        return f"{context.author.display_name} roled a {role_result}. It's getting better and better." \
               f" Your points now: {user.points}"

    @staticmethod
    def action_is_not_ok(guild):
        return f"You do not have enough {guild.points_name}! You need at least {Dice.use_cost}"
