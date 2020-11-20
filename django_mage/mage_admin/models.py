from djongo import models

from config import DJANGO_COGS_PATHS


class SimpleDiscordCommand(models.Model):
    class Meta:
        verbose_name_plural = "Simple Discord Commands"

    name = models.CharField(max_length=30)
    brief = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    output = models.CharField(max_length=500)

    def __str__(self):
        return f'{self.name}'

class SdcSettingsModel(models.Model):
    class Meta:
        verbose_name_plural = "SDC Settings"

    # sdc_path = models.CharField(max_length=30, default=DJANGO_COGS_PATHS)
    sdc_name = models.CharField(max_length=20, default="SDC")

class BotSettingsModel(models.Model):
    class Meta:
        verbose_name_plural = "Bot Settings"

    bot_owner = models.TextField()


class ServerSettingsModel(models.Model):
    class Meta:
        verbose_name_plural = "Server Settings"

    bot_prefix = models.CharField(max_length=5, default="!")
    points_name = models.CharField(max_length=30)
