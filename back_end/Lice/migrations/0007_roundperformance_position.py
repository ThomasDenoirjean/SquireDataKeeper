# Generated by Django 5.0.6 on 2024-05-31 14:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lice', '0006_tournament_match_round_roundperformance'),
    ]

    operations = [
        migrations.AddField(
            model_name='roundperformance',
            name='position',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='Lice.liceposition'),
        ),
    ]
