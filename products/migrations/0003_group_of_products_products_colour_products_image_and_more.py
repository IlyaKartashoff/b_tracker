# Generated by Django 5.0.7 on 2024-07-30 16:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_products_delete_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group_of_products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='products',
            name='colour',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='products',
            name='image',
            field=models.ImageField(blank=True, upload_to='product_photos/'),
        ),
        migrations.AddField(
            model_name='products',
            name='purchase_prise',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=7, null=True),
        ),
        migrations.AddField(
            model_name='products',
            name='quantity',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='products',
            name='sale_prise',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=7, null=True),
        ),
        migrations.AddField(
            model_name='products',
            name='size',
            field=models.IntegerField(choices=[(20, '20 cm'), (30, '30 cm'), (40, '40 cm'), (50, '50 cm'), (60, '60 cm'), (70, '70 cm'), (80, '80 cm'), (100, '100 cm'), (110, '110 cm'), (120, '120 cm'), (130, '130 cm'), (140, '140 cm'), (150, '150 cm')], default=None),
        ),
        migrations.AddField(
            model_name='products',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='products.group_of_products'),
        ),
    ]
