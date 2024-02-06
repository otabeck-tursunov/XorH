from django.db import models


class TogriSoz(models.Model):
    soz = models.CharField(max_length=30)

    def __str__(self):
        return self.soz


class NotogriSoz(models.Model):
    soz = models.CharField(max_length=30)
    t_soz = models.ForeignKey(TogriSoz, on_delete=models.CASCADE)

    def __str__(self):
        return self.soz
