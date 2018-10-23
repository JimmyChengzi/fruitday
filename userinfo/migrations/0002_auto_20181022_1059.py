# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userinfo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('address', models.CharField(max_length=200, verbose_name='地址')),
                ('aname', models.CharField(max_length=50, verbose_name='收件人姓名')),
                ('aphone', models.CharField(max_length=20, verbose_name='收件人手机')),
            ],
        ),
        migrations.AddField(
            model_name='userinfo',
            name='isAcitve',
            field=models.BooleanField(default=True, verbose_name='激活'),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='uemail',
            field=models.EmailField(max_length=254, default='a@a.com', verbose_name='Email'),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='uphone',
            field=models.CharField(max_length=20, default=111, verbose_name='手机'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userinfo',
            name='upwd',
            field=models.CharField(max_length=200, default=111, verbose_name='密码'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='address',
            name='user',
            field=models.ForeignKey(to='userinfo.UserInfo'),
        ),
    ]
