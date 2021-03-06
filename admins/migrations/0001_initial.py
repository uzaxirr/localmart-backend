# Generated by Django 3.2.9 on 2021-11-26 19:04

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Geometry',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(default='Point', max_length=50)),
                ('coordinates', django.contrib.postgres.fields.ArrayField(base_field=models.DecimalField(decimal_places=6, max_digits=9), size=2)),
            ],
        ),
    ]
