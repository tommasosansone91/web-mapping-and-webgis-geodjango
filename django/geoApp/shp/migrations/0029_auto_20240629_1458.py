# Generated by Django 3.1.14 on 2024-06-29 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shp', '0028_auto_20240629_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shp',
            name='shp_file',
            field=models.FileField(upload_to='shp/%Y%m%d_%H%M%S'),
        ),
    ]
