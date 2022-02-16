from django.contrib import admin
from .models import Upload,FileUpload

# Register your models here.
@admin.register(Upload)
class UploadAdmin(admin.ModelAdmin):
    list_display=['timestamp','message']
    list_filter=['timestamp']
# admin.register(Upload,FileUpload)
@admin.register(FileUpload)
class FileUploadAdmin(admin.ModelAdmin):
    list_display=['timestamp','upload_file']
    list_filter=['timestamp']
