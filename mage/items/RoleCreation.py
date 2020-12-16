# from mongoengine import IntField, ReferenceField
# import discord
#
# from mage.models.Item import Item
# from mage.models.User import User
# import utils.data_access as data
#
#
# class RoleCreation(Item):
#     # overriden attributes
#     id = 1
#     name = "rolecreation"
#     brief = 'creates a role and gives you Invites to invite other members'
#     description = 'creates a role and gives you 5 Invites, which you can use to invite other members to your created role'
#     price = 500
#     use_cost = 0
#     level_restriction = 1
#
#     categories = ["Roles"]
#     is_consumable = False
#     is_enabled = True
#     is_event_item = True
#     is_shop_item = True
#
#     #item specific attributes
#     user = ReferenceField(User, null=True)
#     role_id = IntField(null=True, default=None)
#
#     Item.append_categories(categories, is_consumable, is_event_item, level_restriction)
#
#     def __init__(self, *args, **kwargs):
#         super(Item, self).__init__(*args, **kwargs)
#
#     @staticmethod
#     def on_buy(user: User, target: User, amount: int = 0):
#         pass
#
#     @staticmethod
#     def on_use(context, *, role_or_member):
#         user = data.find_one(User, discord_user_id=context.author.id, discord_guild_id=context.guild.id)
#         if user.points >= RoleCreation.use_cost:
#             db_item = data.find_one(RoleCreation, name=RoleCreation.name, )
#             user.points -= RoleCreation.use_cost
#             # todo use
#             if RoleCreation.role_id:
#                 member = role_or_member
#             else:
#                 role_name = role_or_member
#                 RoleCreation.role_name = role_name
#             user.save()
#         else:
#             print(RoleCreation.action_insufficient_points_to_use())
