# Generated by Django 5.2 on 2025-04-30 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0007_product_stripe_price_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='stripe_product_id',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='stripe_price_id',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
