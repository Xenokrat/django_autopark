# Generated by Django 4.1.5 on 2023-01-17 17:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("auto", "0007_alter_vehicle_model"),
    ]

    operations = [
        migrations.CreateModel(
            name="Enterprise",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=255, verbose_name="Название предприятия"
                    ),
                ),
                ("city", models.CharField(max_length=255, verbose_name="Город")),
            ],
        ),
        migrations.AlterField(
            model_name="vehicle",
            name="model",
            field=models.ForeignKey(
                default=2,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="vehicles",
                to="auto.carmodel",
                verbose_name="Бренд",
            ),
        ),
        migrations.CreateModel(
            name="Driver",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=255, verbose_name="Имя")),
                (
                    "second_name",
                    models.CharField(max_length=255, verbose_name="Фамилия"),
                ),
                (
                    "salary",
                    models.PositiveSmallIntegerField(
                        blank=True, null=True, verbose_name="Зарплата"
                    ),
                ),
                (
                    "driving_experience",
                    models.PositiveSmallIntegerField(
                        blank=True, null=True, verbose_name="Водительский"
                    ),
                ),
                (
                    "enterprise",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="drivers",
                        to="auto.enterprise",
                        verbose_name="Предприятие",
                    ),
                ),
                (
                    "vehicle",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="drivers",
                        to="auto.vehicle",
                        verbose_name="Автомобиль",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="vehicle",
            name="current_driver",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="vehicles",
                to="auto.driver",
                verbose_name="Активный водитель",
            ),
        ),
        migrations.AddField(
            model_name="vehicle",
            name="enterprise",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="vehicles",
                to="auto.enterprise",
                verbose_name="Предприятие",
            ),
        ),
    ]
