# Generated by Django 4.0.6 on 2022-08-14 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_customusers_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customusers',
            name='level',
            field=models.CharField(choices=[('0', '0 - New user'), ('2', '2 - Approved User'), ('1', '1 - Verified user'), ('3', '3 - Vip user')], default='0', max_length=1, verbose_name='User Levels'),
        ),
    ]
