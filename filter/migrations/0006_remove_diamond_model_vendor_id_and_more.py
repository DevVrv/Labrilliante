# Generated by Django 4.0.6 on 2022-09-09 13:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('filter', '0005_remove_diamond_model_cert_company_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diamond_model',
            name='vendor_id',
        ),
        migrations.AlterField(
            model_name='diamond_model',
            name='vendor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='vendor_id'),
        ),
    ]
