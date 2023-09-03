from django.db import models


class Material(models.Model):
    material = models.CharField(max_length=255, blank=True,null=True)
    ulchov_briligi = models.CharField(max_length=255,blank=True,null=True)
    miqdori = models.IntegerField(blank=True,null=True)
    narxi = models.IntegerField(blank=True,null=True)
    summasi = models.IntegerField(blank=True,null=True)
