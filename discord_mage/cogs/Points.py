from discord.ext import commands

from discord_mage.commands.points.Profile import Profile
from discord_mage.permissions.IsGuildMessage import IsGuildMessage


class Points(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=Profile.aliases, brief=Profile.brief, description=Profile.description)
    @commands.check(IsGuildMessage.is_guild_message)
    async def profile(self, context):
        await Profile.call(context)


def setup(client):
    client.add_cog(Points(client))
