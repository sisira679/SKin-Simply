# Generated by Django 4.2.6 on 2024-02-29 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skin_app', '0039_delete_ingredient_product_ingredients_product_weight_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='ingredients',
        ),
    ]
