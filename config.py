import os
from pathlib import Path

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
COGS_PATHS = [Path("discord_mage/cogs")]
DJANGO_COGS_PATHS = ROOT_DIR + "/discord_mage/cogs"
DEFAULT_PREFIX = '!'
