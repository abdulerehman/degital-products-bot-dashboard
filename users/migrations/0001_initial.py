# Generated by Django 4.2.7 on 2023-11-15 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=2)),
                ('phone_number', models.CharField(max_length=100)),
            ],
        ),
    ]