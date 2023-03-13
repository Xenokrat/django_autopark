# Generated by Django 4.1.7 on 2023-03-11 10:41

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auto', '0019_alter_enterprise_timezone_gpsautotrack'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gpsautotrack',
            options={'verbose_name': 'GPS Трек', 'verbose_name_plural': 'GPS Треки'},
        ),
        migrations.AlterField(
            model_name='gpsautotrack',
            name='timestamp',
            field=models.DateTimeField(verbose_name='Время записи'),
        ),
        migrations.AlterField(
            model_name='gpsautotrack',
            name='track',
            field=django.contrib.gis.db.models.fields.LineStringField(srid=4326, verbose_name='GPS путь'),
        ),
        migrations.AlterField(
            model_name='gpsautotrack',
            name='vehicle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gps_auto_track', to='auto.vehicle', verbose_name='Авто'),
        ),
    ]
