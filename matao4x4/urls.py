from django.conf.urls.defaults import *
from django.contrib import admin
from matao4x4 import settings

# Uncomment the next two lines to enable the admin:
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^matao4x4/', include('matao4x4.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'^$', 'matao4x4.views.index'),
    (r'^empresa/$', 'matao4x4.views.empresa'),
    (r'^oficina/$', 'matao4x4.views.oficina'),
    (r'^lavajato/$', 'matao4x4.views.lavajato'),
    (r'^localizacao/$', 'matao4x4.views.localizacao'),
    (r'^contato/$', 'matao4x4.views.contato'),
    (r'^acessorios/(?P<tipo_id>\d+)/$', 'matao4x4.views.verAcessorios'),
    (r'^veiculos/(?P<vmarca>[\w_-]+)/$', 'matao4x4.views.verVeiculos'),
    (r'^acessorios/visualizar/(?P<id_acessorios>\d+)/$', 'matao4x4.views.visualizarAc'),
    (r'^veiculos/visualizar/(?P<id_veiculo>\d+)/$', 'matao4x4.views.visualizarVe'),
    (r'^eventos/buscar$', 'matao4x4.views.buscaEvento'),
    (r'^eventos/visualizar/(?P<evento_id>\d+)$', 'matao4x4.views.visualizarEv'),
    (r'^eventosgal/visualizar/(?P<id_evento>\d+)$', 'matao4x4.views.visualizarGa'),
    (r'^news/$', 'matao4x4.views.news'),
    (r'newsletter/$', 'matao4x4.views.newsletter'),
    (r'^equipe/$', 'matao4x4.views.equipe'),
    (r'^expedicao/$', 'matao4x4.views.expedicao'),
    (r'^dicas/$', 'matao4x4.views.dicas'),
    (r'^aconteceu/$', 'matao4x4.views.aconteceu'),
    (r'^veraconteceu/(\d+)/$', 'matao4x4.views.veraconteceu'),
    (r'^eventos/anteriores/$', 'matao4x4.views.eventosant'),
    (r'^mais/eventos/galeria$', 'matao4x4.views.visualizaroutroev'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root' : settings.MEDIA_ROOT}),
    )