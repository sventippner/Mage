
import discord
from discord.ext import commands

from utils.Secrets import Secrets


def main():
    client = discord.ext.commands.Bot(command_prefix='!')
    discord_token = Secrets().get("DISCORD_TOKEN")

    client.run(discord_token)


if __name__ == '__main__':
    main()
