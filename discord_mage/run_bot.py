import os
from pathlib import Path

import discord
from discord.ext import commands

from discord_mage.permissions.IsGuildMessage import IsGuildMessage
from mage.models.Server import Server
from utils.Secrets import Secrets
from config import COGS_PATHS, ROOT_DIR, DEFAULT_PREFIX
from utils.data_access import db_connect, find_one


def get_extensions(path):
    """ yields extensions found in the path folder

    :param path: is the path to the extensions folder
    """
    if Path.exists(Path(f"{ROOT_DIR}/{path}")):
        # module extension are in format Django.cogs.Module
        # we have to convert slashes to points
        ext = str(path).replace('\\', '.')
        ext = str(ext).replace('/', '.')
        for filename in os.listdir(f"{ROOT_DIR}/{path}"):
            if filename.endswith('.py'):
                if not filename.startswith('__init__'):
                    # return cog module name
                    yield str(f"{ext}.{filename[:-3]}")


def load_extensions(client, paths):
    """ Loads cog extensions into the discord bot client

    :param client: is the discord bot
    :param path: is the path to the cogs folder
    """
    for path in paths:
        for ext in get_extensions(path):
            print(f"load {ext}...", end=" ")
            client.load_extension(ext)
            print("success")


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
    load_extensions(client, COGS_PATHS)
    DISCORD_TOKEN = Secrets().get("DISCORD_TOKEN")

    db_connect()

    client.run(DISCORD_TOKEN)


if __name__ == '__main__':
    main()
