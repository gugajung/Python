# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^sincomercio/', include('sincomercio.foo.urls')),
    (r'^$', 'sincomercio.views.index'),
    (r'^quemsomos/', 'sincomercio.views.quem_somos'),
    (r'^servicos/', 'sincomercio.views.servicos'),
    (r'^campanhas/', 'sincomercio.views.campanhas'),
    (r'^contato/', 'sincomercio.views.contato'),
    (r'^localizacao/', 'sincomercio.views.localizacao'),
    (r'^videoteca/$', 'sincomercio.views.videoteca'),
    (r'^lojas/$', 'sincomercio.views.lojas'),
    url(r'^noticias/(?P<fonte>[\w_-]+)/$', 'sincomercio.views.noticias',name="noticias"),
    (r'^acoes-sociais/$', 'sincomercio.views.acoes_sociais'),
    (r'^busca/$', 'sincomercio.views.busca'),
    
    (r'^conhecasincomercio/$','sincomercio.views.conhecasincomercio'),
    
    (r'^midias/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root':settings.MEDIA_ROOT}),
    (r'^midias/arquivos(?P<path>.*)$', 'django.views.static.serve',
        {'document_root':settings.MEDIA_ROOT}),
    
    (r'^links/', 'sincomercio.views.links'),
    url(r'^noticia/(?P<slug>[\w_-]+)/$', 'sincomercio.noticias.views.noticia'),
    (r'^noticiatv/(?P<slug>[\w_-]+)/$', 'sincomercio.noticias.views.noticiatv'),
    (r'^acao-social/(?P<slug>[\w_-]+)/$', 'sincomercio.acoes_sociais.views.acao'),
    (r'^info_video/(?P<video_id>\d+)/$', 'sincomercio.videoteca.views.info_video'),
    (r'^campanha/(?P<slug>[\w_-]+)/$', 'sincomercio.campanhas.views.campanha'),
    (r'^calendario/$', 'sincomercio.views.calendario'),
    (r'^acordo/$', 'sincomercio.views.acordo'),
    (r'^motorista/$', 'sincomercio.views.motorista'),
    (r'^inauguracao/$','sincomercio.views.inauguracao'),
    (r'^repis/$', 'sincomercio.views.repis'),
    (r'^contribuicao/$', 'sincomercio.views.contribuicao'),
    (r'^lercontribuicao/(\d+)/$','sincomercio.views.lercontribuicao'),
    (r'^eventos/(\d+)/$','sincomercio.views.eventos'),
    (r'^eventos/','sincomercio.views.evento'),
    (r'^calendarioMercado/','sincomercio.views.calendarioMercado'),
    (r'^tiposcontribuicao/','sincomercio.views.tipocontribuicao'),
    (r'^cursopalestra/$','sincomercio.views.palestras'),
    (r'^cursopalestra/(\d+)/$','sincomercio.views.palestra'),
    
    # URL para obter o XML por AJAX
    (r'^xml/$','sincomercio.views.getXML'),
    
    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)
