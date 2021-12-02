# Generated by Django 3.2.9 on 2021-11-27 05:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0005_inventory'),
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(default='FeatureCollection', max_length=50)),
                ('geometry', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='admins.geometry')),
                ('properties', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='admins.properites')),
            ],
        ),
    ]