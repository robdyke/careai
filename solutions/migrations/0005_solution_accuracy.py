# Generated by Django 2.1.4 on 2019-02-19 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solutions', '0004_auto_20190109_2015'),
    ]

    operations = [
        migrations.AddField(
            model_name='solution',
            name='accuracy',
            field=models.FloatField(default=0.0),
        ),
    ]
