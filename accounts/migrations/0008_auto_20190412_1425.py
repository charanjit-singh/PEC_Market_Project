# Generated by Django 2.1.7 on 2019-04-12 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20190411_0039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('REJECTED', 'REJECTED'), ('ACCEPTED', 'ACCEPTED'), ('WAITING CONFIRMATION', 'WAITING CONFIRMATION'), ('DELIVERED', 'DELIVERED')], default='WAITING CONFIRMATION', max_length=64),
        ),
    ]
