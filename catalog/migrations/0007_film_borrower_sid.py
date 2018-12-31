# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-12-31 17:14
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_auto_20171115_1308'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='borrower_sid',
            field=models.CharField(blank=True, max_length=7, validators=[django.core.validators.RegexValidator(code='nomatch', message='SID length has to be 7', regex='/^(a|A)([0-9]{6})$/')]),
        ),
    ]