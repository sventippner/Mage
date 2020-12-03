import discord
from discord.ext import commands

from discord_mage.commands.reactions.buttons.distinctbuttons.MakeDistinctRoleButtons import MakeDistinctRoleButtons
from discord_mage.commands.reactions.buttons.makebuttons.MakeRoleButtons import MakeRoleButtons
from discord_mage.permissions.IsGuildMessage import IsGuildMessage


class Reactions(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=MakeRoleButtons.aliases, brief=MakeRoleButtons.brief,
                      description=MakeRoleButtons.description)
    @commands.check(IsGuildMessage.is_guild_message)
    @commands.has_permissions(manage_roles=True, manage_messages=True)
    async def make_role_buttons(self, context, message_id, *args):
        """
        makes an interactive interface using a message, mentioned roles and emojis
        to toggle roles on click of the generated reactions
        :param context: context object automatically passed on function call
        :param message_id: message ID which corresponds to the message that is used to generate reactions
        :param args: contains alternating roles and emojis (first role will be toggled with first emoji and so on)
        """
        await MakeRoleButtons.call(context, self.client, message_id, *args)

    @commands.command(aliases=MakeDistinctRoleButtons.aliases, brief=MakeDistinctRoleButtons.brief,
                      description=MakeDistinctRoleButtons.description)
    @commands.check(IsGuildMessage.is_guild_message)
    @commands.has_permissions(manage_roles=True, manage_messages=True)
    async def make_distinct_role_buttons(self, context, message_id, *args):
        """
        makes an interactive interface using a message, mentioned roles and emojis
        to toggle roles on click of the generated reactions
        :param context: context object automatically passed on function call
        :param message_id: message ID which corresponds to the message that is used to generate reactions
        :param args: contains alternating roles and emojis (first role will be toggled with first emoji and so on)
        """
        await MakeDistinctRoleButtons.call(context, self.client, message_id, *args)


def setup(client):
    client.add_cog(Reactions(client))
