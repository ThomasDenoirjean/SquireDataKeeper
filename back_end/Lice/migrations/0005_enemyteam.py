# Generated by Django 5.0.6 on 2024-05-31 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lice', '0004_alter_fighter_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnemyTeam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
