# Generated by Django 3.2.1 on 2024-09-28 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_alter_appointment_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='note',
            field=models.TextField(blank=True, null=True),
        ),
    ]
