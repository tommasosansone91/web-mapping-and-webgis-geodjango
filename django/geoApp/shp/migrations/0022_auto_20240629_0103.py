# Generated by Django 3.1.14 on 2024-06-29 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shp', '0021_auto_20240628_2319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shp',
            name='shp_file',
            field=models.FileField(upload_to='shp/20240629_010359'),
        ),
    ]
