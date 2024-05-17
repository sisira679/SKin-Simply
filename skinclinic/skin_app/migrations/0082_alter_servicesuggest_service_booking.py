# Generated by Django 4.2.6 on 2024-04-02 12:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('skin_app', '0081_servicesuggest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicesuggest',
            name='service',
            field=models.ForeignKey(default='no treatment needed', on_delete=django.db.models.deletion.CASCADE, to='skin_app.service'),
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_date', models.DateField()),
                ('time_slot', models.TimeField()),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='skin_app.service')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
