# Generated by Django 3.2.18 on 2023-05-06 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='has_data',
            field=models.BooleanField(default=False),
        ),
    ]
