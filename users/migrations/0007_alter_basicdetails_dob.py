# Generated by Django 3.2.5 on 2021-07-20 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20210720_1129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicdetails',
            name='DOB',
            field=models.DateField(default=None, verbose_name='Date of Birthday'),
        ),
    ]