# Generated by Django 3.0.2 on 2020-09-12 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('winem', '0016_auto_20200912_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='stop',
            field=models.BooleanField(default=False),
        ),
    ]