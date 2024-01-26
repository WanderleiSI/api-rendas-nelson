from django.db import models
from django.utils.timezone import now

# Create your models here.
class Renda(models.Model):
    descricao = models.CharField(max_length=100)
    valor = models.FloatField()
    data = models.DateField(default=now)
    usuarioId = models.IntegerField()

    def __str__(self):
        return self.nome