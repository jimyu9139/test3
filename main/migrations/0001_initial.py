# Generated by Django 3.1.7 on 2021-04-09 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='local',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('year', models.CharField(max_length=10)),
                ('month', models.CharField(max_length=10)),
                ('week', models.CharField(max_length=10)),
            ],
        ),
    ]