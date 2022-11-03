# Generated by Django 4.0.6 on 2022-09-19 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_orders_diamond_model_order_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders_diamond_model',
            name='key',
            field=models.CharField(db_index=True, max_length=255, verbose_name='Key'),
        ),
        migrations.AlterField(
            model_name='orders_model',
            name='order_number',
            field=models.CharField(db_index=True, max_length=255, unique=True, verbose_name='Order Number'),
        ),
    ]