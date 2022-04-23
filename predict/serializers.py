from .models import Predict
from rest_framework import serializers


class PredictSerializer(serializers.ModelSerializer):
    model_path = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    data_path = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Predict
        fields = ['model_path', 'data_path']


# class MlModelSerializer(serializers.ModelSerializer):
#     name = serializers.CharField(max_length=50)
#     model_file = serializers.FileField()
#     user = serializers.RelatedField(many=True)
#
#     class Meta:
#         model = MlModel
#         fields = ['name', 'model_file', 'user']
