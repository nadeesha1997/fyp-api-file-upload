# Generated by Django 4.0.4 on 2022-04-13 09:20

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0002_fileupload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fileupload',
            name='upload_file',
            field=cloudinary.models.CloudinaryField(max_length=255),
        ),
    ]
