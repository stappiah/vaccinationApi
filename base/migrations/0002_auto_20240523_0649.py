# Generated by Django 3.2.1 on 2024-05-23 06:49

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospital',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='hospital',
            name='city',
            field=models.CharField(default='Accra', max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hospital',
            name='end_time',
            field=models.TimeField(default=datetime.datetime(2024, 5, 23, 6, 48, 27, 610725, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hospital',
            name='rating',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=1),
        ),
        migrations.AddField(
            model_name='hospital',
            name='start_time',
            field=models.TimeField(default=datetime.datetime(2024, 5, 23, 6, 49, 58, 413721, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
