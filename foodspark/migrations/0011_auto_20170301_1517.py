# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-01 09:47
from __future__ import unicode_literals

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import re


class Migration(migrations.Migration):

    dependencies = [
        ('foodspark', '0010_auto_20170301_1028'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foodqty', models.IntegerField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodspark.Customer')),
                ('fooditem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodspark.FoodItem')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='foodqty',
            field=models.CharField(max_length=500, null=True, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:\\,\\d+)*\\Z'), code='invalid', message='Enter only digits separated by commas.')]),
        ),
        migrations.AlterField(
            model_name='order',
            name='ordertime',
            field=models.TimeField(default=datetime.datetime(2017, 3, 1, 15, 17, 54, 127425)),
        ),
    ]
