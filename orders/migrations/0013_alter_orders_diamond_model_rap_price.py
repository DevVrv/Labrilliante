# Generated by Django 4.0.6 on 2022-09-25 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0012_alter_orders_model_order_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders_diamond_model',
            name='rap_price',
            field=models.IntegerField(blank=True, default=0, verbose_name='Rap Price'),
        ),
    ]
