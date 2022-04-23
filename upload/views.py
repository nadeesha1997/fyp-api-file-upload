from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response

from .models import Upload, FileUpload

from . import serializers


# Create your views here.
class UploadStringView(generics.GenericAPIView):
    serializer_class = serializers.UploadSerializer
    queryset = Upload.objects.all()

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        Uploads = Upload.objects.all()
        serializer = self.serializer_class(instance=Uploads, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class UploadFileView(generics.GenericAPIView):
    serializer_class = serializers.FileUploadSerializer
    queryset = FileUpload.objects.all()

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        uploads = FileUpload.objects.all()
        serializer = self.serializer_class(instance=uploads, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
