# Generated by Django 3.1.7 on 2021-05-07 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0013_auto_20210505_0215'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
