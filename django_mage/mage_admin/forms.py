
from django import forms

from discord_mage.models.SimpleDiscordCommand import SimpleDiscordCommand


class SimpleDiscordCommandForm(forms.Form):
    name = forms.CharField(max_length=30)
    aliases = forms.CharField(max_length=30)
    brief = forms.CharField(max_length=100)
    description = forms.CharField(max_length=200)

    # class Meta:
    #     model = SimpleDiscordCommand
    #     exclude = ()

    def to_document(self):
        # Converts this form to a SimpleDiscordCommand document
        sdc = SimpleDiscordCommand()
        sdc.name = self.name.to_python()
        sdc.aliases = self.aliases.to_python().split(",")
        sdc.brief = self.brief.to_python()
        sdc.description = self.description.to_python()
        return sdc
