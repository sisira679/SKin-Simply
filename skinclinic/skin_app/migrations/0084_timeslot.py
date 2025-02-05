# Generated by Django 4.2.6 on 2024-04-03 06:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('skin_app', '0083_rename_booking_date_booking_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeSlot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time_slot', models.TimeField()),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='skin_app.service')),
            ],
        ),
    ]
