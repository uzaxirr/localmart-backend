# Generated by Django 3.2.9 on 2021-11-28 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0010_inventorymodel_store_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='properitesmodel',
            name='store_state',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
