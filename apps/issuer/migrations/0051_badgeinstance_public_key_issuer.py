# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-11-13 14:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('signing', '0003_auto_20191113_0644'),
        ('issuer', '0050_badgeinstance_identifier'),
    ]

    operations = [
        migrations.AddField(
            model_name='badgeinstance',
            name='public_key_issuer',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='signing.PublicKeyIssuer'),
        ),
    ]
