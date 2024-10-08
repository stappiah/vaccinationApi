# Generated by Django 3.2.1 on 2024-09-13 07:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0003_remove_hospital_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospital',
            name='admin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='administered_hospitals', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Availability',
        ),
    ]
