# Generated by Django 5.0.7 on 2024-09-17 18:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_rename_category_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='products_objects', to='products.group_of_products'),
        ),
    ]
