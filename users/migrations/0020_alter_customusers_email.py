# Generated by Django 4.0.6 on 2022-10-12 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0019_alter_customusers_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customusers',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email'),
        ),
    ]
