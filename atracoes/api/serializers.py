from rest_framework import serializers
from atracoes.models import Local


class AtracaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Local
        fields = [
            'id', 'nome', 'descricao', 'horario_func', 'idade_minima', 'foto'
        ]
