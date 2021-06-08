# Generated by Django 3.2.3 on 2021-05-24 17:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='orderitem',
            name='unique_order_item',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='shop',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='order_shop', to='backend.shop', verbose_name='Магазин'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='product_info',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='product_info',
            field=models.ManyToManyField(default=13, related_name='ordered_items', to='backend.ProductInfo', verbose_name='Информация о продукте'),
        ),
    ]
