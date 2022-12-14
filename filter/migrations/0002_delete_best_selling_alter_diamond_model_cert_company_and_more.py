# Generated by Django 4.0.6 on 2022-08-14 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filter', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Best_Selling',
        ),
        migrations.AlterField(
            model_name='diamond_model',
            name='cert_company',
            field=models.CharField(blank=True, choices=[('0', 'IGI'), ('1', 'GIA'), ('2', 'GCAL'), ('3', 'HDR')], max_length=150, verbose_name='Cert Company'),
        ),
        migrations.AlterField(
            model_name='diamond_model',
            name='clarity',
            field=models.CharField(blank=True, choices=[('0', 'I3'), ('1', 'I2'), ('2', 'I1'), ('3', 'SI2'), ('4', 'SI1'), ('5', 'VS2'), ('6', 'VS1'), ('7', 'VVS2'), ('8', 'VVS1'), ('9', 'IF'), ('10', 'FI')], db_index=True, max_length=150, verbose_name='Clarity'),
        ),
        migrations.AlterField(
            model_name='diamond_model',
            name='color',
            field=models.CharField(blank=True, choices=[('0', 'M'), ('1', 'L'), ('2', 'K'), ('3', 'J'), ('4', 'I'), ('5', 'H'), ('6', 'G'), ('7', 'F'), ('8', 'E'), ('9', 'D')], db_index=True, max_length=150, verbose_name='Color'),
        ),
        migrations.AlterField(
            model_name='diamond_model',
            name='cut',
            field=models.CharField(choices=[('0', 'N/A'), ('1', 'Fair'), ('2', 'Good'), ('3', 'Very Good'), ('4', 'Ideal'), ('5', 'Super Ideal'), ('6', 'Excellent')], max_length=150, verbose_name='Cut'),
        ),
        migrations.AlterField(
            model_name='diamond_model',
            name='fluor',
            field=models.CharField(blank=True, choices=[('0', 'None'), ('1', 'Faint'), ('2', 'Medium'), ('3', 'Strong'), ('4', 'Very Strong')], max_length=150, verbose_name='Fluor'),
        ),
        migrations.AlterField(
            model_name='diamond_model',
            name='polish',
            field=models.CharField(blank=True, choices=[('0', 'Good'), ('1', 'Very Good'), ('2', 'Excellent'), ('3', 'N/A')], max_length=150, verbose_name='Polish'),
        ),
        migrations.AlterField(
            model_name='diamond_model',
            name='shape',
            field=models.CharField(choices=[('0', 'Round'), ('1', 'Marquise'), ('2', 'Asscher'), ('3', 'Cushion'), ('4', 'Emerald'), ('5', 'Heart'), ('6', 'Oval'), ('7', 'Pear'), ('8', 'Princess'), ('9', 'Radiant'), ('10', 'Other')], db_index=True, max_length=150, verbose_name='Shape Name'),
        ),
        migrations.AlterField(
            model_name='diamond_model',
            name='symmetry',
            field=models.CharField(blank=True, choices=[('0', 'N/A'), ('1', 'Good'), ('2', 'Very Good'), ('3', 'Excellent')], max_length=150, verbose_name='Symmetry'),
        ),
    ]
