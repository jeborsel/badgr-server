# Generated by Django 2.2.9 on 2020-05-11 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issuer', '0057_remove_badgeclass_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='badgeinstance',
            name='image',
            field=models.FileField(blank=True, db_index=True, upload_to='uploads/badges'),
        ),
    ]
