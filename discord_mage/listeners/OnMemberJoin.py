from random import choice

import discord
from discord.ext.commands import RoleConverter

from utils import data_access
from mage.models.Server import Server


class OnMemberJoin:

    @staticmethod
    async def call(client, member: discord.Member):
        server = data_access.find_one(Server, discord_guild_id=member.guild.id)
        if server.autorole_role_ids:
            await OnMemberJoin.action_join_autorole(client, server.autorole_role_ids, member)
        if member.guild.system_channel:
            if not member.guild.system_channel_flags.join_notifications:
                if server.guild_welcome_message_enabled:
                    guild_msg = OnMemberJoin.action_guild_welcome_message(server, member)
                    if guild_msg:
                        await member.guild.system_channel.send(guild_msg)
        if server.personal_welcome_message_enabled:
            personal_msg = OnMemberJoin.action_personal_welcome_message(client, server, member)
            if personal_msg:
                await member.send(personal_msg)

    @staticmethod
    def action_guild_welcome_message(server, member: discord.Member):
        msg_list = list(server.guild_welcome_messages)
        msg = None
        if msg_list:
            msg = choice(msg_list)
        return msg

    @staticmethod
    def action_personal_welcome_message(client, server, member: discord.Member):
        msg_list = list(server.personal_welcome_messages)
        msg = None
        if msg_list:
            msg = choice(msg_list)
        return msg

    @staticmethod
    async def action_join_autorole(client, role_ids, member: discord.Member):
        guild = discord.Client.get_guild(client, member.guild.id)
        roles = [guild.get_role(role_id) for role_id in role_ids]
        for role in roles:
            await member.add_roles(role)
