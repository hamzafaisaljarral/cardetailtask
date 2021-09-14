from rest_framework import serializers

from .models import Car, Make, Models, SubModel


class MakeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Make
        fields = '__all__'


class ModelsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Models
        fields = '__all__'


class SubModelSerializer(serializers.ModelSerializer):
    model_id = ModelsSerializer()

    class Meta:
        model = SubModel
        fields = '__all__'


class CarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = '__all__'
