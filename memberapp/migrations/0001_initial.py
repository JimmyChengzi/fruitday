# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=50, verbose_name='商品名称')),
                ('price', models.DecimalField(max_digits=8, decimal_places=2, verbose_name='价格')),
                ('desc', models.TextField(verbose_name='描述')),
                ('picture', models.ImageField(upload_to='static/image/goods', verbose_name='图片')),
                ('isActive', models.BooleanField(default=True, verbose_name='是否上架')),
            ],
        ),
        migrations.CreateModel(
            name='GoodsType',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=50, verbose_name='分类名称')),
                ('picture', models.ImageField(upload_to='static/image/good_type', verbose_name='图片')),
                ('desc', models.TextField(verbose_name='描述')),
                ('isDelete', models.BooleanField(default=False, verbose_name='是否删除')),
            ],
        ),
        migrations.AddField(
            model_name='goods',
            name='type',
            field=models.ForeignKey(to='memberapp.GoodsType'),
        ),
    ]
