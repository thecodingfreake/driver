# Generated by Django 4.1 on 2023-10-11 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_places'),
    ]

    operations = [
        migrations.AddField(
            model_name='driverwork',
            name='update',
            field=models.BooleanField(default=True),
        ),
    ]