import discord
from discord.ext import commands

from discord_mage.commands.AddPoints import AddPoints
from discord_mage.commands.Profile import Profile


class Points(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=Profile.aliases, brief=Profile.brief, description=Profile.description)
    async def profile(self, context):
        await Profile.call(context)

    @commands.command(aliases=AddPoints.aliases, brief=AddPoints.brief, description=AddPoints.description)
    @commands.has_permissions(administrator=True)
    async def add_points(self, context, member: discord.Member, amount: int):
        await AddPoints.call(context, member, amount)




def setup(client):
    client.add_cog(Points(client))
