from os import path, getenv

from dotenv import load_dotenv

from config import ROOT_DIR


class EnvLoader:
    def __init__(self, file_path):
        env_path = path.abspath(path.join(ROOT_DIR, file_path))
        load_dotenv(dotenv_path=env_path)

    """
    Reads and returns a value
    """
    def get(self, constant):
        return getenv(constant)
