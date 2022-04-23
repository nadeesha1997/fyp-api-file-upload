from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from tensorflow import keras

from .models import Predict

from . import serializers


# Create your views here.
class PredictView(generics.GenericAPIView):
    serializer_class = serializers.PredictSerializer
    queryset = Predict.objects.all()

    # def post(self, request):
    #     data = request.data
    #     serializer = self.serializer_class(data=data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(data=serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        # predict = Predict.objects.get(pk=pk)
        predict = Predict.objects.all()
        serializer = self.serializer_class(instance=predict, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


# class UploadModelView(generics.GenericAPIView):
#     serializer_class = serializers.MlModelSerializer
#     queryset = MlModel.objects.all()
#
#     def post(self, request):
#         data = request.data
#         serializer = self.serializer_class(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data, status=status.HTTP_201_CREATED)
#         return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def get(self, request):
#         uploads = MlModel.objects.all()
#         serializer = self.serializer_class(instance=uploads, many=True)
#         return Response(data=serializer.data, status=status.HTTP_200_OK)
