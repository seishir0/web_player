# Generated by Django 4.2 on 2023-04-30 11:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tracklist',
            old_name='localion',
            new_name='location',
        ),
    ]
