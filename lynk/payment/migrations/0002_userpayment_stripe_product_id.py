# Generated by Django 5.2 on 2025-04-30 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userpayment',
            name='stripe_product_id',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
    ]
