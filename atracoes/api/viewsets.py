from rest_framework.viewsets import ModelViewSet
from atracoes.models import Local
from .serializers import AtracaoSerializer
from django_filters.rest_framework import DjangoFilterBackend


class AtracaoViewSet(ModelViewSet):
    queryset = Local.objects.all()
    serializer_class = AtracaoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['nome']
