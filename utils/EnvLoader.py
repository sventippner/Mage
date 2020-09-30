from os import path, getenv
from dotenv import load_dotenv
from config import ROOT_DIR


class EnvLoader:

    def __init__(self, file_path: str):
        """ Loads env file. Filepath starting from ROOT_DIR. """
        env_path = path.abspath(path.join(ROOT_DIR, file_path))

        if path.exists(env_path):
            load_dotenv(dotenv_path=env_path)
        else:
            raise FileNotFoundError(f"File \"{file_path}\" not found. Could not load environment file.")

    def get(self, constant):
        """ Reads and returns a value """
        return getenv(constant)