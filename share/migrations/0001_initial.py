# Generated by Django 4.0.6 on 2022-08-22 04:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ShareModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shareList', models.JSONField(verbose_name='Diamonds Share List')),
                ('shareType', models.CharField(choices=[('0', 'With Prices'), ('1', 'Without Prices')], max_length=1, verbose_name='Share type')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Created Date')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='Updated Date')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User ID')),
            ],
        ),
    ]
