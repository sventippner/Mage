from discord.ext import commands

from discord_mage.commands.Announce import Announce
from discord_mage.commands.Purge import Purge


class Moderation(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(brief=Purge.brief, description=Purge.description)
    @commands.has_permissions(manage_messages=True)
    async def purge(self, context, amount=2):
        await Purge.call(context, amount)

    @commands.command(aliases=Announce.aliases, brief=Announce.brief, description=Announce.description)
    @commands.has_permissions(mention_everyone=True)
    async def announce(self, context, *, message):
        """
        bot announces the message in the announcement channel and mentions @everyone
        requires mention_everyone permission to use
        :param context: context object automatically passed on function call
        :param message: message that is supposed to be announced
        """
        await Announce.call(context, self.client, message)


def setup(client):
    client.add_cog(Moderation(client))

