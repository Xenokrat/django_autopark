# Generated by Django 4.1.5 on 2023-01-15 09:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("auto", "0006_vehicle_model"),
    ]

    operations = [
        migrations.AlterField(
            model_name="vehicle",
            name="model",
            field=models.ForeignKey(
                default=2,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="car_model",
                to="auto.carmodel",
                verbose_name="Бренд",
            ),
        ),
    ]