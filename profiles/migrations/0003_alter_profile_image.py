# Generated by Django 3.2.23 on 2023-12-01 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_rename_update_at_profile_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='../default_profile_aw6v7f', upload_to='images/'),
        ),
    ]
