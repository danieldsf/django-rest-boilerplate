from django.db import models

# Create your models here.
class Configuracao(models.Model):
    ip = models.CharField(max_length=100)
    nome = models.CharField(max_length=200)
    objeto_principal = models.ForeignKey('Obstaculo', on_delete=models.CASCADE)

    def __str__(self):
        return "Nome do Usuário: %s" % (self.nome)

class Ponto(models.Model):
    x = models.FloatField(blank=False, null=False)
    y = models.FloatField(blank=False, null=False)
    objeto = models.ForeignKey('Obstaculo', on_delete=models.CASCADE)

    def __str__(self):
        return "(%s,%s)" % (self.x, self.y)


class Obstaculo(models.Model):
    nome = models.CharField(max_length=200, blank=False, null=False)
    cor = models.CharField(max_length=200, blank=False, null=False)
    tolerancia = models.FloatField(default=50, blank=True, null=True)

    def __str__(self):
        return "%s" % (self.nome)