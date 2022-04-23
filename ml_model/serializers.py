from .models import MlModel, UserModel
from rest_framework import serializers


class MlModelSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=50)
    model_file = serializers.FileField()

    class Meta:
        model = MlModel
        fields = ['name', 'model_file']


class UserModelSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    ml_model = serializers.PrimaryKeyRelatedField(many=True,read_only=True)

    class Meta:
        model = UserModel
        fields = ['user', 'ml_model']
