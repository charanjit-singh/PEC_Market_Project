# Generated by Django 2.1.7 on 2019-04-10 18:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20190410_1522'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
