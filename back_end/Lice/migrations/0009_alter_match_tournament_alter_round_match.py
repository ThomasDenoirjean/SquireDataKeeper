# Generated by Django 5.0.6 on 2024-06-01 06:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lice', '0008_alter_roundperformance_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='tournament',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matchs', to='Lice.tournament'),
        ),
        migrations.AlterField(
            model_name='round',
            name='match',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rounds', to='Lice.match'),
        ),
    ]
