# Generated by Django 4.1 on 2023-09-28 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_driverwork_rename_name_users_driverid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Corporate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=2080)),
            ],
        ),
        migrations.AddField(
            model_name='users',
            name='isadmin',
            field=models.CharField(default='No', max_length=2080),
        ),
    ]
