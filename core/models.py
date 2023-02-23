from django.db import models
from atracoes.models import Local
from comentario.models import Comentario
from avaliacoes.models import Avaliacao
from endereco.models import Endereco


# Create your models here.

class PontoTuristico(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    aprovado = models.BooleanField(default=False)
    local = models.ManyToManyField(Local)
    comentarios = models.ManyToManyField(Comentario)
    avaliacoes = models.ManyToManyField(Avaliacao)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE, null=True, blank=True)
    foto = models.ImageField(upload_to='pontos_turisticos', blank=True, null=True)

    @property
    def descricao_completa2(self):
        return self.nome, self.descricao #verificar

    def __str__(self):
        return self.nome
