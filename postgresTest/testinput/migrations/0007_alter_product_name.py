# Generated by Django 4.2 on 2023-04-18 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testinput', '0006_alter_product_category_alter_product_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
