import os
from pathlib import Path
from config import ROOT_DIR


class Extensions:

    @staticmethod
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

    @staticmethod
    def load_extensions(client, paths):
        """ Loads cog extensions into the discord bot client

        :param client: is the discord bot
        :param path: is the path to the cogs folder
        """
        for path in paths:
            print(f"LOADING\nin path {path}")
            for ext in Extensions.get_extensions(path):
                print(f"load {ext}...", end=" ")
                client.load_extension(ext)
                print("success")\

    @staticmethod
    def unload_extensions(client, paths):
        """ Loads cog extensions into the discord bot client

        :param client: is the discord bot
        :param path: is the path to the cogs folder
        """
        for path in paths:
            print(f"UNLOADING\nin path {path}")
            for ext in Extensions.get_extensions(path):
                print(f"unload {ext}...", end=" ")
                client.unload_extension(ext)
                print("success")