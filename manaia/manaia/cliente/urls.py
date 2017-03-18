#pylint: disable=E1120
from django.conf.urls.defaults import patterns, url
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required


def urls():
    urlpatterns = patterns('',
        url(r'^$','manaia.views.AreaCliente', name="areacliente"),
        url(r'login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html','authentication_form': AuthenticationForm}, name='login'),
        url(r'logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'},name="logout"),
        url(r'^arquivos/$','manaia.views.AreaClienteAjax', name="viewareacliente"),
        url(r'^pesquisar/$','manaia.views.PesquisaAreaClienteAjax', name="viewareacliente"),
    )
    
    return urlpatterns