# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userinfo', '0002_auto_20181022_1059'),
        ('memberapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('ccount', models.IntegerField(verbose_name='数量')),
                ('goods', models.ForeignKey(to='memberapp.Goods')),
                ('user', models.ForeignKey(to='userinfo.UserInfo')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('orderNo', models.CharField(max_length=50, verbose_name='订单号')),
                ('cals', models.TextField(verbose_name='订单商品描述')),
                ('orderStatus', models.IntegerField(default=1, verbose_name='订单状态', choices=[(1, '未支付'), (2, '已支付'), (3, '已取消'), (4, '已完成')])),
                ('user', models.ForeignKey(to='userinfo.UserInfo')),
            ],
        ),
    ]
