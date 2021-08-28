# rest framework
from rest_framework import serializers
# models
from .models import ExtractedData

class ExtractedDataSerializer(serializers.ModelSerializer):
    """ ExtractedData Serializer """

    class Meta:
        model = ExtractedData
        fields = '__all__'
