from rest_framework import serializers
from endereco.models import Endereco


class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = [
            'linha1', 'linha2', 'cidade', 'estado', 'pais', 'latitude', 'longitude'
        ]
