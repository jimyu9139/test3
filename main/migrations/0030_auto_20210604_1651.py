# Generated by Django 3.1.7 on 2021-06-04 08:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0029_govern_code'),
    ]

    operations = [
        migrations.RenameField(
            model_name='govern',
            old_name='code',
            new_name='codename',
        ),
    ]
