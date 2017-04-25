# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('noble_metal', '0004_auto_20170412_2312'),
    ]

    operations = [
        migrations.AddField(
            model_name='goldprice',
            name='situation',
            field=models.IntegerField(default=-1, choices=[(-1, '其他'), (0, '跌'), (1, '涨'), (2, '2-8凹槽'), (3, '8-14凹槽'), (4, '14-20凹槽')]),
        ),
    ]
