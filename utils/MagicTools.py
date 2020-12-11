import importlib
import os
from pathlib import Path

from config import ROOT_DIR
from mage.models import Item
from mage.items import *


def get_files_in_dir(dir_path):
    """ Returns a list of every python file in given directory
    """
    files = []
    if Path.exists(Path(f"{ROOT_DIR}/{dir_path}")):
        for filename in os.listdir(f"{ROOT_DIR}/{dir_path}"):
            if filename.endswith('.py'):
                if not filename.startswith('__init__'):
                    file = str(f"{filename[:-3]}")
                    files.append(file)

    return files


def create_instance_of_item(name: str):
    try:
        return create_instance(f"mage.items.{name}", name)
    except Exception:
        return None


def create_instance(module: str, classname: str):
    """ Returns an instance of the class """

    try:
        cls = getattr(importlib.import_module(module), classname)
    except Exception:
        raise ValueError(f"Error: Could not load class. {classname} in {module}")

    return cls
