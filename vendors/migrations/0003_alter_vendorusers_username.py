# Generated by Django 4.0.6 on 2022-09-03 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0002_rename_vendor_name_vendorusers_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendorusers',
            name='username',
            field=models.CharField(max_length=255, unique=True, verbose_name='Vendor Name'),
        ),
    ]
