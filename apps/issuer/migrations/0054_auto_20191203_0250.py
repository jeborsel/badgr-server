# Generated by Django 2.2.7 on 2019-12-03 10:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issuer', '0053_auto_20191126_0212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='badgeclass',
            name='image',
            field=models.FileField(blank=True, upload_to='uploads/badges'),
        ),
        migrations.AlterField(
            model_name='badgeclass',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='badgeinstance',
            name='acceptance',
            field=models.CharField(choices=[('Unaccepted', 'Unaccepted'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected')], default='Unaccepted', max_length=254),
        ),
        migrations.AlterField(
            model_name='badgeinstance',
            name='image',
            field=models.FileField(blank=True, upload_to='uploads/badges'),
        ),
        migrations.AlterField(
            model_name='badgeinstance',
            name='public_key_issuer',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='signing.PublicKeyIssuer'),
        ),
        migrations.AlterField(
            model_name='badgeinstance',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='issuer',
            name='badgrapp',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainsite.BadgrApp'),
        ),
        migrations.AlterField(
            model_name='issuer',
            name='faculty',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='institution.Faculty'),
        ),
        migrations.AlterField(
            model_name='issuer',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='uploads/issuers'),
        ),
        migrations.AlterField(
            model_name='issuer',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
    ]
