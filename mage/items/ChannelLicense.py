from mongoengine import IntField, ReferenceField
import discord

from mage.models.Item import Item
from mage.models.User import User
import utils.data_access as data


class ChannelLicense(Item):
    # overriden attributes
    name = "Channel_License"
    brief = 'item, which creates a server Category with 3 default channels'
    description = 'creates a server category with 3 default channels. Channel and Category Names depend on the custom name you choose'
    price = 500
    use_cost = 100
    level_restriction = 30

    categories = ["Roles"]
    is_consumable = True
    is_enabled = True
    is_event_item = True
    is_shop_item = True

    Item.append_categories(categories, is_consumable, is_event_item, level_restriction)

    def __init__(self, *args, **kwargs):
        super(Item, self).__init__(*args, **kwargs)

    @staticmethod
    def on_buy():
        pass

    @classmethod
    async def on_use(cls, context, name):
        user = data.find_one(User, discord_user_id=context.author.id, discord_guild_id=context.guild.id)
        ok = ChannelLicense.pre_use(user)
        guild = context.guild
        if not (name.isascii() and name.isprintable() and '"' not in name and "'" not in name and 1 <= len(name) <= 18):
            ok = False
        for category in guild.categories:
            if name.lower() in category.name.lower():
                ok = False
                break
        if ok:
            cls.pay_use_cost(user)
            if cls.is_consumable:
                user.lose_item(cls.name)
            user.save()
            await ChannelLicense.action_is_ok(context, guild, name)
        else:
            await context.send(ChannelLicense.action_is_not_ok())

    @staticmethod
    async def action_is_ok(context, guild, name):
        category = await guild.create_category(name)
        channel = await category.create_text_channel(name=rf"text1-{name}")
        await category.create_text_channel(name=rf"text2-{name}")
        await category.create_voice_channel(name=rf"{name}")
        await channel.send(ChannelLicense.action_success(name, context.author))

    @staticmethod
    def action_success(name, author):
        return f"created new category: {name}\n{author.mention}"

    @staticmethod
    def action_is_not_ok():
        return "You dont meet the Requirements or you have used invalid arguments"
