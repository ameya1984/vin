from vindecoder.models import Vin
from rest_framework import serializers


class VinSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vin
        fields = ['variable', 'variableId', 'value', 'valueId']
