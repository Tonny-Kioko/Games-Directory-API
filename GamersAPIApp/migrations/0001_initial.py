# Generated by Django 3.2.20 on 2023-09-19 08:06

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('genre', models.CharField(max_length=100)),
                ('release_date', models.DateField()),
                ('publisher', models.CharField(max_length=100)),
                ('platform', models.CharField(max_length=100)),
                ('rating', models.PositiveIntegerField(default=5, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
    ]