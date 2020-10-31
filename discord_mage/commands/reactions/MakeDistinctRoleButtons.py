from discord.ext.commands import RoleConverter

from mage.models.Message import Message
from mage.models.Reaction import Reaction
from utils import data_access


class MakeDistinctRoleButtons:
    aliases = ['makedistinctbuttons', 'makedistinctrolebuttons']
    brief = "members can toggle roles"
    description = "creates emoji buttons (reactions) below the message. Members can toggle roles upon reaction."

    @staticmethod
    async def call(context, client, message_id, *args):
        if len(args) % 2 != 0:
            await context.send(MakeDistinctRoleButtons.action_wrong_input())
        else:
            new_reactions = await MakeDistinctRoleButtons.action_generate_reactions(context, *args)
            discord_message = await context.channel.fetch_message(message_id)
            status_new = await MakeDistinctRoleButtons.action_make_message_document(context, discord_message,
                                                                                    new_reactions)
            if discord_message.author == client.user:
                await MakeDistinctRoleButtons.action_edit_message(new_reactions, discord_message, status_new)
            for reaction in new_reactions:
                await discord_message.add_reaction(reaction[0])
            await context.message.delete()

    @staticmethod
    def action_wrong_input():
        return "Wrong input!"

    @staticmethod
    async def action_generate_reactions(context, *args):
        role_converter = RoleConverter()
        roles = [await role_converter.convert(context, arg) for arg in args[::2]]
        emojis = [arg for arg in args[1::2]]
        return [reaction for reaction in zip(emojis, roles)]

    @staticmethod
    async def action_edit_message(reactions, discord_message, status_new):
        string = "\n\n-----------------------------------------\nPress emojis for role assignment:\nOnly one role can be active at a time!" if status_new else ""
        for reaction in reactions:
            string += f"\n{reaction[0]}\t\t{reaction[1].mention}"
        await discord_message.edit(content=discord_message.content + string)

    @staticmethod
    async def action_make_message_document(context, discord_message, new_reactions):
        message = data_access.find_one(Message, discord_message_id=discord_message.id,
                                       discord_guild_id=context.guild.id)
        if message:
            status_new = False
            reactions = message.reactions
        else:
            status_new = True
            message = Message(discord_message_id=discord_message.id, discord_guild_id=context.guild.id)
            reactions = []
            message.is_distinct = True
        for reaction in new_reactions:
            emoji, role = reaction
            reactions.append(Reaction(emoji, role.id))
        message.reactions = reactions
        message.save()
        return status_new
