# Generated by Django 4.2.6 on 2024-02-19 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skin_app', '0030_alter_product_quality'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='quality',
            field=models.CharField(default=True, max_length=100),
        ),
    ]
