# Generated by Django 3.0.8 on 2020-07-13 08:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='phone',
            new_name='number',
        ),
    ]
