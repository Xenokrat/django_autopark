# Generated by Django 4.1.7 on 2023-03-11 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auto', '0020_alter_gpsautotrack_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gpsautotrack',
            name='timestamp',
        ),
        migrations.AddField(
            model_name='gpsautotrack',
            name='timestamp_end',
            field=models.DateTimeField(null=True, verbose_name='Время прибытия'),
        ),
        migrations.AddField(
            model_name='gpsautotrack',
            name='timestamp_start',
            field=models.DateTimeField(null=True, verbose_name='Время отправления'),
        ),
    ]
