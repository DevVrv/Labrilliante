# Generated by Django 4.0.6 on 2022-08-17 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_orders_model_hold_hours_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders_model',
            name='order_number',
            field=models.CharField(db_index=True, max_length=255, verbose_name='Order Number'),
        ),
    ]