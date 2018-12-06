from django.contrib import admin
from django.contrib.auth.models import User, Group
from solo.admin import SingletonModelAdmin
from .models import *

admin.site.site_header = 'Labrador'

admin.site.site_title = 'Labrador'

admin.site.index_title = 'Inicio'

admin.site.register(Configuracao, SingletonModelAdmin)

admin.site.register([Obstaculo, Ponto, Log])

#admin.site.unregister(User)
#admin.site.unregister(Group)