# Generated by Django 3.1.7 on 2021-04-26 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20210424_1601'),
    ]

    operations = [
        migrations.AddField(
            model_name='local',
            name='number',
            field=models.CharField(default='', max_length=10),
        ),
    ]
