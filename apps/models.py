from django.db import models


class Material(models.Model):
    num = models.IntegerField()
    material = models.CharField(max_length=555, null=False)
    ulchov = models.CharField(max_length=555)
    miqdori = models.IntegerField()
    narxi = models.IntegerField()
    summasi = models.IntegerField()
    tashkilot = models.CharField(max_length=500, blank=True, null=True)
