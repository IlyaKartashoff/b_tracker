# Generated by Django 5.0.7 on 2024-08-01 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_alter_products_size'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='group_of_products',
            options={'verbose_name': 'Группа товаров', 'verbose_name_plural': 'Группы товаров'},
        ),
        migrations.AlterModelOptions(
            name='products',
            options={'verbose_name': 'Продукт', 'verbose_name_plural': 'Продукты'},
        ),
        migrations.AlterField(
            model_name='group_of_products',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='Группа товаров'),
        ),
        migrations.AlterModelTable(
            name='group_of_products',
            table='groups_of_products',
        ),
    ]
