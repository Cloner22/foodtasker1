# Generated by Django 5.2 on 2025-05-28 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coreapp', '0008_rename_locations_driver_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='location',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
