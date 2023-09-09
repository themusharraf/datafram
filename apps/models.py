from django.db import models


class Material(models.Model):
    PLAN_TYPE = (
        ('кг', 'Килограмм'),
        ('км', 'киллометр'),
        ('литр', 'Литр'),
        ('м', 'Метры'),
        ('тн', 'Тонна '),
        ('шт', 'Штука'),
        ('МЛ', 'МиллиЛитр'),
        ('м2', 'Метр квадрат'),
        ('м3', 'метры куб'),
        ('пач', 'пачка'),
        ('к-т', 'комплект'),
        ('кв.м', 'Квадратные метры'),
        ('Қоп', 'ҚОП'),
        ('набор', 'набор'),
        ('п/м', 'Погонные метры'),
        ('ваг', 'вагон'),
        ('кВтч', 'кВтч'),
        ('пар', 'пара'),
        ('М/Ч', 'Машина час'),
        ('шт/уп', 'Штука. (упаковка)'),
        ('Банка ', 'Банка-310миллиграм'),
        ('бухт ', 'бухт'),
    )
    cod = models.CharField(max_length=255)
    material = models.CharField(max_length=555, null=False)
    ulchov = models.CharField(choices=PLAN_TYPE, max_length=200)
    miqdori = models.IntegerField(blank=True, null=True)
    narxi = models.IntegerField(default=0)
    summasi = models.IntegerField( blank=True, null=True)
    tashkilot = models.CharField(max_length=500, blank=True, null=True)

