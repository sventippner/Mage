from datetime import datetime, timedelta

import discord
from discord.ext import commands
from discord.ext.commands import RoleConverter

from discord_mage.commands.events.StartEvent import StartEvent
from mage.models.ParticipatingRole import ParticipatingRole


class Event(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.group()
    async def event(self, context):
        print("event")

    @event.group()
    @commands.has_permissions(administrator=True)
    async def start(self, context):
        print("start")

    @start.command()
    @commands.has_permissions(administrator=True)
    async def now(self, context, name, duration: int, rewards: int, *, participating_roles):
        start_date = datetime.now()
        end_date = start_date + timedelta(days=duration)
        role_converter = RoleConverter()
        roles = [await role_converter.convert(context, role) for role in participating_roles.split()]
        role_participant_list = [ParticipatingRole(role.id, [member.id for member in role.members], 0) for role in roles]
        rewards = [rewards]
        await StartEvent.call(context, name, start_date, end_date, rewards, role_participant_list)


def setup(client):
    client.add_cog(Event(client))
