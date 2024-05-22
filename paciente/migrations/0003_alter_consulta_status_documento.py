# Generated by Django 5.0.4 on 2024-05-21 20:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("paciente", "0002_rename_consukta_consulta"),
    ]

    operations = [
        migrations.AlterField(
            model_name="consulta",
            name="status",
            field=models.CharField(
                choices=[
                    ("A", "Agendado"),
                    ("F", "Finalizada"),
                    ("C", "Cancelada"),
                    ("I", "Iniciada"),
                ],
                default="A",
                max_length=1,
            ),
        ),
        migrations.CreateModel(
            name="Documento",
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
                ("titulo", models.CharField(max_length=30)),
                ("documento", models.FileField(upload_to="documentos")),
                (
                    "consulta",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="paciente.consulta",
                    ),
                ),
            ],
        ),
    ]
