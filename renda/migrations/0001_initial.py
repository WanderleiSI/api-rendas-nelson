# Generated by Django 5.0.1 on 2024-01-26 02:50

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Renda",
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
                ("descricao", models.CharField(max_length=100)),
                ("valor", models.FloatField()),
                ("data", models.DateField(default=django.utils.timezone.now)),
                ("usuarioId", models.IntegerField()),
            ],
        ),
    ]
