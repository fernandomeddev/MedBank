# Generated by Django 3.2.5 on 2021-07-20 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210720_0917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicdetails',
            name='annual_income',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='status',
            name='balance',
            field=models.FloatField(default=10000.0),
        ),
    ]
