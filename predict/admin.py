from django.contrib import admin
from .models import Predict


# Register your models here.
# @admin.register(MlModel)
# class MlModelAdmin(admin.ModelAdmin):
#     list_display = ['model_path', 'data_path']
#     list_filter = ['model_path', 'data_path']


@admin.register(Predict)
class PredictAdmin(admin.ModelAdmin):
    list_display = ['model_path', 'data_path']
    list_filter = ['model_path', 'data_path']
