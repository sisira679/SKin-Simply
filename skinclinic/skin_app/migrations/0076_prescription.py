# Generated by Django 4.2.6 on 2024-04-01 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('skin_app', '0075_delete_prescription'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dosage', models.CharField(max_length=50)),
                ('duration', models.CharField(max_length=50)),
                ('appointment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prescriptions', to='skin_app.appointment')),
                ('medicine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='skin_app.product')),
            ],
        ),
    ]
