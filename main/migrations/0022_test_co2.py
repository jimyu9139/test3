# Generated by Django 3.1.7 on 2021-05-24 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_test_pm'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='CO2',
            field=models.CharField(default='', max_length=10),
        ),
    ]
