# Generated by Django 3.0.2 on 2020-08-19 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('winem', '0004_auto_20200818_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='by',
            field=models.IntegerField(default=11),
            preserve_default=False,
        ),
    ]