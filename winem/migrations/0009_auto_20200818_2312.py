# Generated by Django 3.0.2 on 2020-08-19 03:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('winem', '0008_team_banned'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='vote',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='winem.Team'),
        ),
    ]
