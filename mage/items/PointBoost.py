from mage.models.Item import Item
from mage.models.User import User
from mage.models.XPMultiplier import XPMultiplier
from utils import data_access
import datetime


class PointBoost(Item):
    # overriden attributes
    name = "PointBoost"
    brief = 'item, which grants you bonus Points per message'
    description = 'item, which grants you bonus Points per message'
    price = 100
    use_cost = 0
    level_restriction = 0

    categories = ["Boost"]
    is_consumable = True
    is_enabled = False
    is_event_item = True
    is_shop_item = True

    # item specific
    BOOST_FACTOR=2
    TIMEDELTA = datetime.timedelta(days=7)

    Item.append_categories(categories, is_consumable, is_event_item, level_restriction)

    def __init__(self, *args, **kwargs):
        super(Item, self).__init__(*args, **kwargs)

    @staticmethod
    def on_buy():
        pass

    @classmethod
    async def on_use(cls, context):
        user = data_access.find_one(User, discord_user_id=context.author.id, discord_guild_id=context.guild.id)
        ok = cls.pre_use(user)
        already_exists = data_access.find_one(XPMultiplier, discord_user_id=context.author.id,
                                              discord_guild_id=context.guild.id)
        if ok:
            if already_exists:
                await context.send(cls.already_exists())
            else:
                if cls.is_consumable:
                    user.lose_item(cls.name)
                user.save()
                await cls.create_new_xpmultiplier(context)
        else:
            await context.send(cls.action_is_not_ok())

    @staticmethod
    def action_success(multiplier, end_date):
        return f"You now gain {multiplier} times the amount of points per message until {end_date}."

    @staticmethod
    def action_is_not_ok():
        return "You don't meet the Item requirements or the item is disabled."

    @staticmethod
    def already_exists():
        return "You already have an active Point Boost."

    @classmethod
    async def create_new_xpmultiplier(cls, context):
        boost = cls.BOOST_FACTOR
        end_date = (datetime.datetime.today() + cls.TIMEDELTA)
        new_xp_mult = XPMultiplier(discord_user_id=context.author.id, discord_guild_id=context.guild.id, multiplier=boost, end_date=end_date)
        new_xp_mult.save()
        await context.send(PointBoost.action_success(new_xp_mult.multiplier, new_xp_mult.end_date))
