# Generated by Django 3.0.2 on 2020-09-12 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('winem', '0015_temp_used'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='phone',
            field=models.TextField(default='bruh'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='stop',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]