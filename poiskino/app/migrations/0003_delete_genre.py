# Generated by Django 3.1.4 on 2020-12-17 09:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_film_ggenre'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Genre',
        ),
    ]
