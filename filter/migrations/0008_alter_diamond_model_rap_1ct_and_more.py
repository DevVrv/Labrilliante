# Generated by Django 4.0.6 on 2022-09-16 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filter', '0007_diamond_model_is_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diamond_model',
            name='rap_1ct',
            field=models.IntegerField(verbose_name='Rap_1ct'),
        ),
        migrations.AlterField(
            model_name='diamond_model',
            name='sale_price',
            field=models.IntegerField(verbose_name='Sale Price'),
        ),
    ]