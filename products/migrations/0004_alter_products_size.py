# Generated by Django 5.0.7 on 2024-07-30 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_group_of_products_products_colour_products_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='size',
            field=models.IntegerField(blank=True, choices=[(20, '20 cm'), (30, '30 cm'), (40, '40 cm'), (50, '50 cm'), (60, '60 cm'), (70, '70 cm'), (80, '80 cm'), (100, '100 cm'), (110, '110 cm'), (120, '120 cm'), (130, '130 cm'), (140, '140 cm'), (150, '150 cm')], default=20),
        ),
    ]
