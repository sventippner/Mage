from discord.ext.commands import RoleConverter

from mage.models.Message import Message
from mage.models.Reaction import Reaction
from utils import data_access


class MakeRoleButtons:
    aliases = ['makebuttons', 'makerolebuttons']
    brief = "members can toggle roles"
    description = "creates emoji buttons (reactions) below the message. Members can toggle roles upon reaction."

    @staticmethod
    async def call(context, client, message_id, *args):
        if len(args) % 2 != 0:
            await context.send('Wrong input!')
        else:
            role_converter = RoleConverter()
            roles = [await role_converter.convert(context, arg) for arg in args[::2]]
            emojis = [arg for arg in args[1::2]]
            if len(roles) == len(emojis):
                message = await context.channel.fetch_message(message_id)
                msg = Message(discord_message_id=message_id, discord_guild_id=context.guild.id)
                m = []
                for emoji, role in zip(emojis, roles):
                    await message.add_reaction(emoji)
                    m.append(Reaction(emoji, str(role)))    # todo fix DB
                msg.reactions = m
                msg.save()

                await context.message.delete()
                if message.author == client.user:
                    string = "\n\n-----------------------------------------\nPress emojis for role assignment:"
                    for i in range(len(roles)):
                        string += f"\n{emojis[i]}\t\t{roles[i].mention}"
                    await message.edit(content=message.content + string)
            else:
                context.send('Wrong input!')
