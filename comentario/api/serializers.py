from rest_framework import serializers
from comentario.models import Comentario


class ComentarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comentario
        fields = [
           'usuario', 'comentario', 'data', 'aprovado'
        ]
