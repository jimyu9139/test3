# Generated by Django 3.1.7 on 2021-05-20 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_auto_20210520_2213'),
    ]

    operations = [
        migrations.AddField(
            model_name='local',
            name='CO2',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='local',
            name='PM',
            field=models.CharField(default='', max_length=10),
        ),
    ]