# Generated by Django 3.0.2 on 2020-08-17 06:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('winem', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='away',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='away_games', to='winem.Team'),
        ),
        migrations.AlterField(
            model_name='game',
            name='home',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='home_games', to='winem.Team'),
        ),
        migrations.AlterField(
            model_name='game',
            name='week',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='games', to='winem.Weeks'),
        ),
        migrations.AlterField(
            model_name='pick',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='picks', to='winem.Game'),
        ),
        migrations.AlterField(
            model_name='pick',
            name='picker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='picks', to='winem.Student'),
        ),
    ]
