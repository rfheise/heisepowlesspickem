# Generated by Django 3.0.2 on 2020-08-18 20:45

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('winem', '0003_remove_student_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pick',
            name='game',
        ),
        migrations.AddField(
            model_name='game',
            name='time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='pick',
            name='team',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='picks', to='winem.Team'),
        ),
        migrations.AddField(
            model_name='pick',
            name='week',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='picks', to='winem.Weeks'),
        ),
        migrations.AddField(
            model_name='student',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4),
        ),
        migrations.AddField(
            model_name='team',
            name='by',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='teambyweeks', to='winem.Weeks'),
        ),
        migrations.AddField(
            model_name='team',
            name='nfc',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='weeks',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4),
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='winem.Student')),
            ],
        ),
    ]