# Generated by Django 3.0.2 on 2020-08-19 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('winem', '0007_remove_game_game_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='banned',
            field=models.BooleanField(default=False),
        ),
    ]
