import discord
from discord.ext import commands
from utils.Secrets import Secrets


def main():
    client = discord.ext.commands.Bot(command_prefix='!')
    DISCORD_TOKEN = Secrets().get("DISCORD_TOKEN")
    client.run(DISCORD_TOKEN)


if __name__ == '__main__':
    main()
