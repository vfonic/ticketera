# Generated by Django 3.2.9 on 2023-04-17 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='max_transfer_datetime',
            new_name='transfers_enabled_until',
        ),
    ]
