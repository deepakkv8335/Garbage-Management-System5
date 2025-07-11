# Generated by Django 5.0.6 on 2025-02-13 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_remove_booking_rating_remove_booking_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='status',
            field=models.CharField(choices=[('pending', 'pending'), ('waiting', 'waiting'), ('approved', 'approved'), ('picked', 'picked'), ('reject', 'reject')], default='pending', max_length=50),
        ),
    ]
