# Generated by Django 5.0.4 on 2024-05-19 00:14

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("medico", "0003_datasabertas"),
        ("paciente", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Consukta",
            new_name="Consulta",
        ),
    ]