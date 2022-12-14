# Generated by Django 4.0.6 on 2022-09-09 13:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('filter', '0004_alter_maxmin_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diamond_model',
            name='cert_company',
        ),
        migrations.RemoveField(
            model_name='diamond_model',
            name='color_comment',
        ),
        migrations.RemoveField(
            model_name='diamond_model',
            name='comments',
        ),
        migrations.RemoveField(
            model_name='diamond_model',
            name='fluorescence',
        ),
        migrations.RemoveField(
            model_name='diamond_model',
            name='gridle_from',
        ),
        migrations.RemoveField(
            model_name='diamond_model',
            name='gridle_to',
        ),
        migrations.RemoveField(
            model_name='diamond_model',
            name='gridle_type',
        ),
        migrations.RemoveField(
            model_name='diamond_model',
            name='on_memo',
        ),
        migrations.RemoveField(
            model_name='diamond_model',
            name='origin',
        ),
        migrations.RemoveField(
            model_name='diamond_model',
            name='rap_price',
        ),
        migrations.RemoveField(
            model_name='diamond_model',
            name='report_link',
        ),
        migrations.RemoveField(
            model_name='diamond_model',
            name='shape_ex',
        ),
        migrations.RemoveField(
            model_name='diamond_model',
            name='warehouse',
        ),
        migrations.AddField(
            model_name='diamond_model',
            name='girdle',
            field=models.CharField(default=0, max_length=255, verbose_name='Gridle'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='diamond_model',
            name='lab',
            field=models.CharField(default=1, max_length=255, verbose_name='Lab'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='diamond_model',
            name='measurements',
            field=models.CharField(default=23, max_length=255, verbose_name='Measurements'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='diamond_model',
            name='best_selling',
            field=models.BooleanField(default=0, verbose_name='Best Selling'),
        ),
        migrations.AlterField(
            model_name='diamond_model',
            name='cert_number',
            field=models.CharField(max_length=255, verbose_name='Cert Number'),
        ),
        migrations.AlterField(
            model_name='diamond_model',
            name='clarity',
            field=models.CharField(max_length=255, verbose_name='Clarity'),
        ),
        migrations.AlterField(
            model_name='diamond_model',
            name='color',
            field=models.CharField(max_length=255, verbose_name='Color'),
        ),
        migrations.AlterField(
            model_name='diamond_model',
            name='culet',
            field=models.CharField(max_length=255, verbose_name='Culet'),
        ),
        migrations.AlterField(
            model_name='diamond_model',
            name='cut',
            field=models.CharField(max_length=255, verbose_name='Cut'),
        ),
        migrations.AlterField(
            model_name='diamond_model',
            name='depth',
            field=models.CharField(max_length=255, verbose_name='Depth'),
        ),
        migrations.AlterField(
            model_name='diamond_model',
            name='depth_procent',
            field=models.CharField(max_length=255, verbose_name='Depth %'),
        ),
        migrations.AlterField(
            model_name='diamond_model',
            name='disc',
            field=models.CharField(max_length=255, verbose_name='Discount'),
        ),
        migrations.AlterField(
            model_name='diamond_model',
            name='fluor',
            field=models.CharField(max_length=255, verbose_name='Fluour'),
        ),
        migrations.AlterField(
            model_name='diamond_model',
            name='length',
            field=models.CharField(max_length=255, verbose_name='Length'),
        ),
        migrations.AlterField(
            model_name='diamond_model',
            name='lw',
            field=models.CharField(max_length=255, verbose_name='L/W'),
        ),
        migrations.AlterField(
            model_name='diamond_model',
            name='photo',
            field=models.URLField(verbose_name='Image URL'),
        ),
        migrations.AlterField(
            model_name='diamond_model',
            name='polish',
            field=models.CharField(max_length=255, verbose_name='Polish'),
        ),
        migrations.AlterField(
            model_name='diamond_model',
            name='rap_1ct',
            field=models.CharField(max_length=255, verbose_name='Rap_1ct'),
        ),
        migrations.AlterField(
            model_name='diamond_model',
            name='ref',
            field=models.CharField(max_length=255, verbose_name='Ref'),
        ),
        migrations.AlterField(
            model_name='diamond_model',
            name='sale_price',
            field=models.CharField(max_length=255, verbose_name='Sale Price'),
        ),
        migrations.AlterField(
            model_name='diamond_model',
            name='shape',
            field=models.CharField(max_length=255, verbose_name='Shape'),
        ),
        migrations.AlterField(
            model_name='diamond_model',
            name='symmetry',
            field=models.CharField(max_length=255, verbose_name='Symmetry'),
        ),
        migrations.AlterField(
            model_name='diamond_model',
            name='table_procent',
            field=models.CharField(max_length=255, verbose_name='Table %'),
        ),
        migrations.AlterField(
            model_name='diamond_model',
            name='vendor',
            field=models.CharField(max_length=255, verbose_name='Vendor'),
        ),
        migrations.AlterField(
            model_name='diamond_model',
            name='vendor_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='vendor_id'),
        ),
        migrations.AlterField(
            model_name='diamond_model',
            name='video',
            field=models.URLField(verbose_name='Video URL'),
        ),
        migrations.AlterField(
            model_name='diamond_model',
            name='weight',
            field=models.CharField(max_length=255, verbose_name='Weight'),
        ),
        migrations.AlterField(
            model_name='diamond_model',
            name='width',
            field=models.CharField(max_length=255, verbose_name='Width'),
        ),
    ]
