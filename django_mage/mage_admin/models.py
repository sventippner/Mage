from djongo import models


class SimpleDiscordCommand(models.Model):
    class Meta:
        verbose_name_plural = "Simple Discord Commands"

    name = models.CharField(max_length=30)
    brief = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    output = models.CharField(max_length=500)

    def __str__(self):
        return f'{self.name}'


class BotSettingsModel(models.Model):
    class Meta:
        verbose_name_plural = "Bot Settings"

    bot_owner = models.TextField()


class ServerSettingsModel(models.Model):
    class Meta:
        verbose_name_plural = "Server Settings"

    discord_server_id = models.CharField(max_length=200)
    prefix = models.CharField(max_length=30)
    points_name = models.CharField(max_length=30)
    bot_owner = models.TextField()


class SdcSettingsModel(models.Model):
    class Meta:
        verbose_name_plural = "SDC Settings"

    sdc_path = models.CharField(max_length=30)
    sdc_name = models.CharField(max_length=20)