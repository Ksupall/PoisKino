# Generated by Django 2.0.4 on 2020-05-26 07:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20200525_1748'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='list',
            name='name',
        ),
    ]
