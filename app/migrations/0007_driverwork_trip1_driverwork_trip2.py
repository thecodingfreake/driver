# Generated by Django 4.1 on 2023-10-11 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_driverwork_update'),
    ]

    operations = [
        migrations.AddField(
            model_name='driverwork',
            name='trip1',
            field=models.CharField(default='-', max_length=2080),
        ),
        migrations.AddField(
            model_name='driverwork',
            name='trip2',
            field=models.CharField(default='-', max_length=2080),
        ),
    ]