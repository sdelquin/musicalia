# Generated by Django 5.0.3 on 2024-03-31 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracks', '0002_remove_track_singer_track_artist'),
    ]

    operations = [
        migrations.AddField(
            model_name='track',
            name='num_visits',
            field=models.PositiveBigIntegerField(default=0),
        ),
    ]
