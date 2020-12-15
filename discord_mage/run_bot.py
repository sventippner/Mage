import os
from pathlib import Path

import discord
from discord.ext import commands

from discord_mage.permissions.IsGuildMessage import IsGuildMessage
from mage.models.Server import Server
from utils.Extensions import Extensions
from utils.Secrets import Secrets
from config import COGS_PATHS, ROOT_DIR, DEFAULT_PREFIX
from utils.data_access import db_connect, find_one





def init_intents():
    intents = discord.Intents.default()
    intents.members = True
    return intents


def main():
    intents = init_intents()
    client = discord.ext.commands.Bot(
        intents=intents,
        command_prefix=lambda _, context: find_one(Server, discord_guild_id=context.guild.id).bot_prefix if IsGuildMessage.is_guild_message(context) else DEFAULT_PREFIX
    )
    Extensions.load_extensions(client, COGS_PATHS)
    DISCORD_TOKEN = Secrets().get("DISCORD_TOKEN")

    db_connect()

    client.run(DISCORD_TOKEN)


if __name__ == '__main__':
    main()
