from djongo import models


class SimpleDiscordCommand(models.Model):
    class Meta:
        verbose_name_plural = "Simple Disord Commands"

    name = models.CharField(max_length=30)
    brief = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    output = models.CharField(max_length=500)

    def __str__(self):
        return f'{self.name}'
