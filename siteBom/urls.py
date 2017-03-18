from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^siteBom/', include('siteBom.foo.urls')),

    (r'^$', 'siteBom.views.index'),
    (r'^dicas/$', 'siteBom.dicas.views.index'),
    (r'^sobre/$', 'siteBom.views.sobre'),
    (r'^faleconosco/$', 'siteBom.views.faleConosco'),
    (r'^redecredenciada/$', 'siteBom.views.redeCred'),
    (r'^localizacao/$', 'siteBom.views.localizacao'),
    (r'^enquetes/$','siteBom.enquetes.views.index'),
    # VIEW DE DETALHES DA ENQUETE
    (r'^enquetes/(?P<slug>[\w_-]+)/$', 'siteBom.enquetes.views.enquete'),
    # VIEW PARA OS RESULTADOS
    (r'^enquetes/(?P<slug>[\w_-]+)/resultados/$', 'siteBom.enquetes.views.resultados'),
    # VIEW PARA VOTAR
    (r'^enquetes/(?P<slug>[\w_-]+)/votar/$', 'siteBom.enquetes.views.votar'),
    (r'^midias/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root':settings.MEDIA_ROOT}),
        
    # VIEW DE DETALHES DA DICA
    (r'^dicas/(?P<slug>[\w_-]+)/$', 'siteBom.dicas.views.dica'),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)
