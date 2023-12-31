# Generated by Django 4.1.5 on 2023-08-06 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoiceapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoicedetail',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
        migrations.AlterField(
            model_name='invoicedetail',
            name='unit_price',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
    ]
