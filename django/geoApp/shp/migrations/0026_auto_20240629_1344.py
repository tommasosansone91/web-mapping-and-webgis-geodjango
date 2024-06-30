# Generated by Django 3.1.14 on 2024-06-29 13:44

from django.db import migrations, models
import shp.configs


class Migration(migrations.Migration):

    dependencies = [
        ('shp', '0025_auto_20240629_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shp',
            name='shp_file',
            field=models.FileField(upload_to=shp.configs.generate_uploaded_shp_file_relpath),
        ),
    ]