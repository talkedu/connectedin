from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^perfis/(?P<perfil_id>\d+)$', exibir, name='exibir')
]
