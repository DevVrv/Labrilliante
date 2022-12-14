# Generated by Django 4.0.6 on 2022-08-22 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_alter_orders_model_total_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders_model',
            name='order_status',
            field=models.CharField(choices=[('0', 'Rejected'), ('1', 'On verification'), ('2', 'Order accepted'), ('3', 'Delivery is in progress'), ('4', 'Delivered'), ('5', 'Completed')], db_index=True, default='1', max_length=1, verbose_name='Order Status'),
        ),
        migrations.AlterField(
            model_name='orders_model',
            name='order_type',
            field=models.CharField(choices=[('0', 'COD'), ('1', 'Invocie'), ('2', 'Cash Memo'), ('3', 'Memo'), ('4', 'Hold')], db_index=True, max_length=1, verbose_name='Order Type'),
        ),
    ]
