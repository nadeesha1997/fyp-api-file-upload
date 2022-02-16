from pyexpat import model
from .models import Upload,FileUpload
from rest_framework import serializers

class UploadSerializer(serializers.ModelSerializer):
    timestamp=serializers.CharField(max_length=20)
    message=serializers.CharField(max_length=500)

    class Meta:
        model=Upload
        fields=['timestamp','message']

class FileUploadSerializer(serializers.ModelSerializer):
    timestamp=serializers.CharField(max_length=20)
    upload_file=serializers.FileField()

    class Meta:
        model=FileUpload
        fields=['timestamp','upload_file']
