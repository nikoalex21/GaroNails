# Generated by Django 5.1.2 on 2024-11-27 03:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spa', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicio',
            name='imagen',
        ),
    ]
