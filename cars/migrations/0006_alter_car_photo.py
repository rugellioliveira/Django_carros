# Generated by Django 5.0.2 on 2024-02-18 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cars", "0005_alter_car_photo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="car",
            name="photo",
            field=models.ImageField(
                blank=True,
                default="cars/imagem_padrao.jpg",
                null=True,
                upload_to="cars/",
            ),
        ),
    ]