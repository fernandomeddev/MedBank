# Generated by Django 3.2.5 on 2021-07-20 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_moneytransfer_enter_the_amount_to_be_transferred_in_inr'),
    ]

    operations = [
        migrations.AddField(
            model_name='basicdetails',
            name='complete_name',
            field=models.CharField(blank=True, default=None, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='basicdetails',
            name='cpf',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='basicdetails',
            name='last_name',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
    ]
