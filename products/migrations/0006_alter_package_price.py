# Generated by Django 4.2.7 on 2023-11-18 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_remove_product_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='price',
            field=models.IntegerField(),
        ),
    ]