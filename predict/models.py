from django.db import models
from upload.models import FileUpload
from ml_model.models import UserModel


# Create your models here.
class Predict(models.Model):
    model_path = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    data_path = models.ForeignKey(FileUpload, on_delete=models.CASCADE)


# class MlModel(models.Model):
#     name = models.CharField(max_length=50)
#     model_file = models.FileField(upload_to='models')
#     user = models.ForeignKey(User, on_delete=models.DO_NOTHING)


def __str__(self):
    return f"<selected model: {self.model_path} data file: {self.message}>"
