# Generated by Django 5.0.6 on 2024-05-29 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lice', '0002_alter_fighter_first_tournament'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fighter',
            name='first_tournament',
            field=models.DateField(blank=True, null=True),
        ),
    ]
