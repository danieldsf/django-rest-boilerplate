from django.db import models
from solo.models import SingletonModel

# Create your models here.
class Configuracao(SingletonModel):
    ip = models.CharField(max_length=100)
    nome_espaco = models.CharField(max_length=200)
    nome_usuario = models.CharField(max_length=200)
    escala_pixels_centimetros = models.FloatField(blank=False, null=False)
    objeto_principal = models.OneToOneField('Obstaculo', on_delete=models.CASCADE, related_name='configuracao')

    def __str__(self):
        return "Nome do Usuário: %s" % (self.nome_usuario)
    
    @property
    def is_danger(self):
        return len(self.objeto_principal.ponto.lados_livres) < 4

class Ponto(models.Model):
    x = models.FloatField(blank=False, null=False)
    y = models.FloatField(blank=False, null=False)
    date_added = models.DateTimeField(auto_now=True)
    obstaculo = models.OneToOneField('Obstaculo', on_delete=models.CASCADE, related_name='ponto')

    def __str__(self):
        return "(%s,%s)" % (self.x, self.y)
    
    @property
    def direcao(self):
        pass    
    
    @property
    def lados_livres(self):
        return (0,1,2,3)

class Obstaculo(models.Model):
    nome = models.CharField(max_length=200, blank=False, null=False)
    cor_maxima = models.CharField(max_length=200, blank=False, null=False)
    cor_minima = models.CharField(max_length=200, blank=False, null=False)
    raio = models.FloatField(blank=False, null=False)
    
    def __str__(self):
        return "%s" % (self.nome)

class Log(models.Model):
    obstaculo = models.ForeignKey('Obstaculo', on_delete=models.CASCADE, related_name='logs')
    x = models.FloatField(blank=False, null=False)
    y = models.FloatField(blank=False, null=False)
    date_added = models.DateTimeField(auto_now=True)
    descricao = models.CharField(max_length=255, blank=False)
	
    def __str__(self):
        return "%s em %s" % (self.descricao, self.date_added)