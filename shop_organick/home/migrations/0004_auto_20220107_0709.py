# Generated by Django 3.2.11 on 2022-01-07 07:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_category_product'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'категория'},
        ),
        migrations.AlterModelOptions(
            name='homepage',
            options={'verbose_name': 'homepage'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Продукт'},
        ),
    ]