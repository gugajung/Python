'''
Created on 04/12/2012

@author: User
'''
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext
from django.utils.decorators import method_decorator
from manaia.banner.models import Banner
from manaia.forms import FormContato, FormNewsletter
from manaia.links.models import Link, Categoria
from manaia.noticias.models import Noticia
from django.contrib.auth.tests.decorators import LoginRequiredTestCase
from django.contrib.auth.decorators import login_required
from manaia.arquivo.models import Arquivos
from manaia.arquivo.models import Categoria as CategoriasConsulta
from django.db.models.query_utils import Q
from django.core import serializers
#from manaia.utils.auxiliares import cria_paginacao

def index(request):
    
    banner = Banner.objects.filter(status='A').all()
    
    noticias = Noticia.objects.filter(status='A').all().order_by("-id")[0:6]
    
    linksUteis = Link.objects.filter(nomecategoria = 7).all().order_by("site_nome")
    
    categorias = Categoria.objects.all();
    
    if request.method == 'POST': 
        
        form = FormNewsletter(request.POST)
        
        if form.is_valid():
            form.save();
            
    else:
        form = FormNewsletter()
    return render_to_response('index.html', locals(), context_instance=RequestContext(request))

def NoticiasOnline(request):
    
    banner = Banner.objects.filter(status='A').all()
    
    noticias = Noticia.objects.filter(status='A').all()
    
    return render_to_response('noticiasonline.html', locals(), context_instance=RequestContext(request))

def AreaRestrita(request):
    
    
    return render_to_response('arearegistra.html', locals(), context_instance=RequestContext(request))

def Localizacao(request):
    
    banner = Banner.objects.filter(status='A').all()
    
    return render_to_response('localizacao.html', locals(), context_instance=RequestContext(request))

def Empresa(request):
    
    banner = Banner.objects.filter(status='A').all() 
    
    return render_to_response('empresa.html', locals(), context_instance=RequestContext(request))


def Equipe(request):
    
    banner = Banner.objects.filter(status='A').all() 
    
    return render_to_response('equipe.html', locals(), context_instance=RequestContext(request))

def Servicos(request):
    
    banner = Banner.objects.filter(status='A').all() 
    
    return render_to_response('servicos.html', locals(), context_instance=RequestContext(request))


def VerNoticias(request,id):
    
    banner = Banner.objects.filter(status='A').all() 
    
    Vernoticia = Noticia.objects.filter(pk=id )
    
    return render_to_response('VerNoticias.html', locals(), context_instance=RequestContext(request))

def VerLinks(request):
    
    categorias = Categoria.objects.all()
    
    return render_to_response('VerLinks.html', locals(), context_instance=RequestContext(request))


def Busca(request):
    
    banner = Banner.objects.filter(status='A').all()  
    
    q = request.GET.get("busca")
    q2 = request.GET.get("busca")
        
    if q:            
        lista_noticias = Noticia.objects.filter(titulo__icontains=q)
        lista_noticias2 = Noticia.objects.filter(conteudo__icontains=q)
        
        if q2:
            lista_links = Link.objects.filter(site_nome__icontains=q2)

        else:
            redirect("/busca/?busca=")     
            
            
    
    return render_to_response('busca.html', locals(), context_instance=RequestContext(request))

def Contato(request):
    
    banner = Banner.objects.filter(status='A').all() 
    
    form = FormContato()
    
    if request.method == 'POST': 
        
        form = FormContato(request.POST)
        
        if form.is_valid():
            
            form.enviar()
            classe = 'sucesso'
            mensagem = 'Seu email foi enviado com sucesso !!'
            
            form = FormContato()
            
        else: 
            
            mensagem = 'Erro ao enviar mensagem !!'
            
    return render_to_response('contato.html', locals(), context_instance=RequestContext(request))

@login_required(login_url='/login/')
def AreaCliente(request):
    arquivos = Arquivos.objects.filter(cliente = request.user.pk)
    categorias = CategoriasConsulta.objects.all()
    usuario = request.user;
    return render_to_response('areacliente.html', locals(), context_instance=RequestContext(request))

@login_required(login_url='/login/')
def AreaClienteAjax(request):
        try:
            obj = Arquivos.objects.filter(Q(categoria=request.POST['valorCategoria']) & Q(cliente = request.user.pk))
        except:
            obj = ""
        _json = serializers.serialize("json", obj)   
        #_json = json.dumps({"nome": nome, "id_medico":id_medico})
        return HttpResponse(_json, "application/json")    

@login_required(login_url='/login/')
def PesquisaAreaClienteAjax(request):
        try:
            obj = Arquivos.objects.filter(nome__contains = request.POST['pesquisaInput']);
        except:
            obj = ""
        _json = serializers.serialize("json", obj)   
        #_json = json.dumps({"nome": nome, "id_medico":id_medico})
        return HttpResponse(_json, "application/json")
    
