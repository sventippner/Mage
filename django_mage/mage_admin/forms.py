"""
from django.forms import *

from discord_mage.models.SimpleDiscordCommand import SimpleDiscordCommand


class SimpleDiscordCommandForm(ModelForm):
    class Meta:
        model = SimpleDiscordCommand
        exclude = ()
"""