# Generated by Django 5.0.6 on 2024-07-04 11:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lice', '0015_alter_fighter_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roundperformance',
            name='round',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='round_perfomances', to='Lice.round'),
        ),
    ]
