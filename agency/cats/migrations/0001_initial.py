# Generated by Django 5.1.2 on 2024-10-30 17:00

import cats.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SpyCat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('experience', models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(15)])),
                ('breed', models.CharField(max_length=50, validators=[cats.validators.validate_breed])),
                ('salary', models.FloatField()),
            ],
        ),
    ]