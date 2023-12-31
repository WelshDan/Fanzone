# Generated by Django 3.2.23 on 2023-12-16 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supported', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamsList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team', models.CharField(choices=[('arsenal', 'Arsenal'), ('aston_villa', 'Aston Villa'), ('bournemouth', 'Bournemouth'), ('brentford', 'Brentford'), ('brighton', 'Brighton'), ('burnley', 'Burnley'), ('chelsea', 'Chelsea'), ('crystal_palace', 'Crystal Palace'), ('everton', 'Everton'), ('fulham', 'Fulham'), ('liverpool', 'Liverpool'), ('luton_town', 'Luton Town'), ('man_city', 'Man City'), ('man_utd', 'Man Utd'), ('newcastle', 'Newcastle'), ('notts_forest', 'Notts Forest'), ('sheff_utd', 'Sheff Utd'), ('tottenham', 'Tottenham'), ('west Ham', 'West Ham'), ('wolves', 'Fulham')], max_length=40, unique=True)),
                ('league', models.IntegerField(choices=[('arsenal', 'Arsenal'), ('aston_villa', 'Aston Villa'), ('bournemouth', 'Bournemouth'), ('brentford', 'Brentford'), ('brighton', 'Brighton'), ('burnley', 'Burnley'), ('chelsea', 'Chelsea'), ('crystal_palace', 'Crystal Palace'), ('everton', 'Everton'), ('fulham', 'Fulham'), ('liverpool', 'Liverpool'), ('luton_town', 'Luton Town'), ('man_city', 'Man City'), ('man_utd', 'Man Utd'), ('newcastle', 'Newcastle'), ('notts_forest', 'Notts Forest'), ('sheff_utd', 'Sheff Utd'), ('tottenham', 'Tottenham'), ('west Ham', 'West Ham'), ('wolves', 'Fulham')])),
            ],
        ),
    ]
