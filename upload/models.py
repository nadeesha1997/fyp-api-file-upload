from django.db import models


# Create your models here.
class Upload(models.Model):
    timestamp = models.CharField(max_length=20)
    message = models.CharField(max_length=500)


class FileUpload(models.Model):
    timestamp = models.CharField(max_length=20)
    upload_file = models.FileField(upload_to='db')


def __str__(self):
    return f"<Upload data {self.timestamp} message: {self.message}>"
