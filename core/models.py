from django.db import models

# Create your models here.
class Configuracao(models.Model):
    ip = models.CharField(max_length=100)
    nome_espaco = models.CharField(max_length=200)
    nome_usuario = models.CharField(max_length=200)
    escala_pixels_centimetros = models.FloatField(blank=False, null=False)
    objeto_principal = models.ForeignKey('Obstaculo', on_delete=models.CASCADE)

    def __str__(self):
        return "Nome do Usuário: %s" % (self.nome)
    
    @property
    def is_danger(self):
        return True

class Ponto(models.Model):
    x = models.FloatField(blank=False, null=False)
    y = models.FloatField(blank=False, null=False)
    objeto = models.ForeignKey('Obstaculo', on_delete=models.CASCADE)
    
    def __str__(self):
        return "(%s,%s)" % (self.x, self.y)
    
    @property
    def direcao(self):
        pass    
    
    @property
    def lados_livres(self):
        pass

class Obstaculo(models.Model):
    nome = models.CharField(max_length=200, blank=False, null=False)
    cor_maxima = models.CharField(max_length=200, blank=False, null=False)
    cor_minima = models.CharField(max_length=200, blank=False, null=False)
    raio = models.FloatField(blank=False, null=False)

    def __str__(self):
        return "%s" % (self.nome)

class Log(models.Model):
	descricao = models.CharField(max_length=255, blank=False)
	date_added = models.DateTimeField(auto_now=True)

	def __str__(self):
		return "%s em %s" % (self.descricao, self.date_added)