# Generated by Django 3.1.7 on 2021-06-04 08:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0030_auto_20210604_1651'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='govern',
            name='codename',
        ),
    ]
