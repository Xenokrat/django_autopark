# Generated by Django 4.1.5 on 2023-02-01 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auto", "0015_alter_manager_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="vehicle",
            name="photo",
            field=models.ImageField(
                blank=True, null=True, upload_to="photos/%Y/%m/%d/", verbose_name="Фото"
            ),
        ),
    ]
