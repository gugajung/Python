from django.conf import settings
from django.conf.urls.defaults import patterns, include, url
from manaia.cliente.urls import urls as urlsClientes

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.contrib.auth.forms import AuthenticationForm
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'manaia.views.home', name='home'),
    # url(r'^manaia/', include('manaia.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
      url(r'^admin/', include(admin.site.urls)),
      (r'^$', 'manaia.views.index'),
      (r'^noticias/onlines/$', 'manaia.views.NoticiasOnline'),
      (r'^area/restrita/$', 'manaia.views.AreaRestrita'),
      (r'^localizacao/$', 'manaia.views.Localizacao'),
      (r'^empresa/$', 'manaia.views.Empresa'),
      (r'^equipe/$', 'manaia.views.Equipe'),
      (r'^servicos/$', 'manaia.views.Servicos'),
      (r'^contato/$', 'manaia.views.Contato'),
      (r'^VerNoticias/(\d+)/$', 'manaia.views.VerNoticias'),
      (r'^VerLinks/$', 'manaia.views.VerLinks'),
      (r'^buscar/$', 'manaia.views.Busca'),
      (r'^buscar/$', 'manaia.views.Busca'),
      (r'^areacliente/', include(urlsClientes())),
      url(r'login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html','authentication_form': AuthenticationForm}, name='login'),
)


if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root' : settings.MEDIA_ROOT}),
    )
