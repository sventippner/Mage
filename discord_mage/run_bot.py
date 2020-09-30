import os
from pathlib import Path

import discord
from discord.ext import commands

from utils.Secrets import Secrets
from config import COGS_PATH, ROOT_DIR


# returns names of cog modules
def get_extensions(path):
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


# loads cog modules into client
def load_modules(client, path):
    for ext in get_extensions(path):
        print(f"load {ext}...", end=" ")
        client.load_extension(ext)
        print("success")


def main():
    client = discord.ext.commands.Bot(command_prefix='!')

    load_modules(client, COGS_PATH)

    DISCORD_TOKEN = Secrets().get("DISCORD_TOKEN")
    client.run(DISCORD_TOKEN)


if __name__ == '__main__':
    main()
