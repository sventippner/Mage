from os import path, getenv
import discord
from discord.ext import commands
from dotenv import load_dotenv


def main():
    client = discord.ext.commands.Bot(command_prefix='!')
    env_path = path.abspath(path.join(__file__, "../../secrets/secrets.env"))
    load_dotenv(dotenv_path=env_path)
    discord_token = getenv("DISCORD_TOKEN")
    client.run(discord_token)


if __name__ == '__main__':
    main()
