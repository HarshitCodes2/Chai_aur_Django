# Generated by Django 4.2.14 on 2024-08-08 11:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChaiVariety',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='chais/')),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('type', models.CharField(choices=[('ML', 'MASALA CHAI'), ('GR', 'GINGER'), ('PL', 'PLAIN'), ('EL', 'ELAICHI')], max_length=2)),
            ],
        ),
    ]
