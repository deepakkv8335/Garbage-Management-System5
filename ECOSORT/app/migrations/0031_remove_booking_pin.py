# Generated by Django 5.0.6 on 2025-02-17 11:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0030_remove_booking_icon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='pin',
        ),
    ]
