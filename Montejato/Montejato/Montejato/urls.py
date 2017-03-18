from django.conf import settings
from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin

# Uncomment the next two lines to enable the admin:
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Montejato.views.home', name='home'),
    # url(r'^Montejato/', include('Montejato.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
     url(r'^$', 'Montejato.views.index'),
     url(r'^jateamento/', 'Montejato.views.Jateamento'),
     url(r'^construcao/', 'Montejato.views.Construcao'),
     url(r'^montagem/', 'Montejato.views.Montagem'),
     url(r'^contato/', 'Montejato.views.Contato'),
     url(r'^parceiros/', 'Montejato.views.Parceiros'),
     url(r'^servicos/', 'Montejato.views.Servicos'),
     url(r'^empresa/', 'Montejato.views.Empresa'),
      
)

#if settings.DEBUG:
#    urlpatterns += patterns('',
#        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root' : settings.MEDIA_ROOT}),
#    )
