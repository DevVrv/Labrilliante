# Generated by Django 4.0.6 on 2022-09-19 12:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0006_alter_orders_model_order_status_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders_Diamond_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref', models.CharField(max_length=255, verbose_name='Ref')),
                ('cert_number', models.CharField(max_length=255, verbose_name='Cert Number')),
                ('shape', models.CharField(max_length=255, verbose_name='Shape')),
                ('clarity', models.CharField(max_length=255, verbose_name='Clarity')),
                ('color', models.CharField(max_length=255, verbose_name='Color')),
                ('rap_1ct', models.IntegerField(blank=True, verbose_name='Rap_1ct')),
                ('sale_price', models.IntegerField(blank=True, verbose_name='Sale Price')),
                ('disc', models.FloatField(verbose_name='Discount')),
                ('girdle', models.CharField(max_length=255, verbose_name='Gridle')),
                ('weight', models.FloatField(max_length=255, verbose_name='Weight')),
                ('cut', models.CharField(max_length=255, verbose_name='Cut')),
                ('polish', models.CharField(max_length=255, verbose_name='Polish')),
                ('symmetry', models.CharField(max_length=255, verbose_name='Symmetry')),
                ('culet', models.CharField(max_length=255, verbose_name='Culet')),
                ('fluor', models.CharField(max_length=255, verbose_name='Fluour')),
                ('length', models.FloatField(verbose_name='Length')),
                ('width', models.FloatField(verbose_name='Width')),
                ('depth', models.FloatField(verbose_name='Depth')),
                ('lw', models.FloatField(verbose_name='L/W')),
                ('measurements', models.CharField(max_length=255, verbose_name='Measurements')),
                ('lab', models.CharField(max_length=255, verbose_name='Lab')),
                ('depth_procent', models.FloatField(blank=True, verbose_name='Depth %')),
                ('table_procent', models.FloatField(blank=True, verbose_name='Table %')),
                ('photo', models.URLField(verbose_name='Image URL')),
                ('video', models.URLField(verbose_name='Video URL')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated date')),
                ('key', models.CharField(db_index=True, max_length=255, unique=True, verbose_name='Key')),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Buyer')),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.orders_model', verbose_name='Order ID')),
            ],
            options={
                'verbose_name': 'Diamond',
                'verbose_name_plural': 'Diamonds',
                'ordering': ['sale_price'],
            },
        ),
    ]
