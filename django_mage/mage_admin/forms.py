from django import forms

from django_mage.mage_admin.models import SimpleDiscordCommand, BotSettingsModel, ServerSettingsModel, SdcSettingsModel


class SimpleDiscordCommandForm(forms.ModelForm):
    class Meta:
        model = SimpleDiscordCommand
        exclude = ()


class BotSettingsForm(forms.ModelForm):
    class Meta:
        model = BotSettingsModel
        exclude = ()


class ServerSettingsForm(forms.ModelForm):
    class Meta:
        model = ServerSettingsModel
        exclude = ()


class SdcSettingsForm(forms.ModelForm):
    class Meta:
        model = SdcSettingsModel
        exclude = ()
