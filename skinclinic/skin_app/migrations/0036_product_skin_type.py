# Generated by Django 4.2.6 on 2024-02-28 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skin_app', '0035_product_created_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='skin_type',
            field=models.CharField(choices=[('Dry', 'Dry'), ('Oily', 'Oily'), ('Normal', 'Normal'), ('Combination', 'Combination'), ('Sensitive', 'Sensitive')], default=True, max_length=50),
        ),
    ]
