from rest_framework import serializers
from .models import BioOutput




class BioSerializer(serializers.ModelSerializer):
    class Meta:
        model = BioOutput
        fields = (
            'protien', 'smile'
        )


class BioSerializer2(serializers.ModelSerializer):
    class Meta:
        model = BioOutput
        fields = (
            'num1',
            'num2'
        )