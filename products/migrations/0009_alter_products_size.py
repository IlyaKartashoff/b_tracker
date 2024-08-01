# Generated by Django 5.0.7 on 2024-08-01 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_alter_products_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='size',
            field=models.CharField(choices=[('20 cm', '20 cm'), ('30 cm', '30 cm'), ('40 cm', '40 cm')], default=20, max_length=250),
        ),
    ]
