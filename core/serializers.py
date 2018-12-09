from rest_framework import serializers
from .models import *

class PontoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ponto
        fields = ('x', 'y', 'date_added', 'obstaculo')

class ObstaculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Obstaculo
        fields = ('x', 'y', 'date_added', 'obstaculo')

class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = ('x', 'y', 'date_added', 'obstaculo')

class ConfiguracaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Configuracao
        fields = ('x', 'y', 'date_added', 'obstaculo')
