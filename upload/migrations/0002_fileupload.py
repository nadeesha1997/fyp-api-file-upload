# Generated by Django 4.0.2 on 2022-02-07 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.CharField(max_length=20)),
                ('upload_file', models.FileField(upload_to='')),
            ],
        ),
    ]
