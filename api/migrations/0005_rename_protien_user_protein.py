# Generated by Django 3.2.18 on 2023-05-13 20:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_rename_fibres_user_fibers'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='protien',
            new_name='protein',
        ),
    ]
