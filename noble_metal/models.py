# coding=utf-8
from django.db import models
from django.conf import settings


class GoldPrice(models.Model):
    date = models.DateField(db_index=True)
    time = models.TimeField()
    price = models.FloatField()
    dtype = models.IntegerField(
        default=1, choices=settings.DTYPE, db_index=True)
    situation = models.IntegerField(
        default=1000, choices=settings.SITUATION)

    class Meta:
        unique_together = [("date", "dtype")]
        db_table = 'gold_price'
        verbose_name = '黄金高低位价格时间表'

    def __unicode__(self):
        return self.date

    def __str__(self):
        return '{0}_{1}'.format(
            self.date, dict(settings.DTYPE)[self.dtype])
