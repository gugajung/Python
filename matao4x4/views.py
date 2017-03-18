from datetime import datetime
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.shortcuts import render_to_response, get_object_or_404
from django.template.context import RequestContext
from django.views.generic.simple import redirect_to
from matao4x4.acessorios.models import TipoAcessorio, Acessorio, FotosAcessorio
from matao4x4.anuncios.models import Anunciante, Evento
from matao4x4.banners.models import Banner
from matao4x4.eventos.models import Eventos, ImagemGaleria, GaleriaEvento
from matao4x4.forms import FormContato, FormAcessorio, FormVeiculo, \
    FormNewsletter
from matao4x4.veiculos.models import Veiculos
from matao4x4.aconteceu.models import Aconteceu, ConteudoAconteceu

class Anunciantes(object):
    anunciantes = Anunciante.objects.all().order_by('?')[:6]
    
    
def index(request):
    
    anuncios = Anunciantes()
    banners = Banner.objects.all()
    listaTipoAc = TipoAcessorio.objects.all()
    
    
    tituloeventos = Eventos.objects.all().order_by('-id')[:6]
    capa = ImagemGaleria.objects.filter(capa = 1).order_by('-id')[:6]
    
    
    eventosDestaque = Evento.objects.filter(data__month = datetime.now().month).order_by('-data')[0:1]
    eventos = Evento.objects.order_by('-id')[0:4]
    
    
    return render_to_response('index.html', locals(), context_instance=RequestContext(request))

def empresa(request):
    
    banners = Banner.objects.all()
    anuncios = Anunciantes()
    
    
    return render_to_response('empresa.html', locals(),  context_instance=RequestContext(request))

def oficina(request):
    
    banners = Banner.objects.all()
    anuncios = Anunciantes()
    
    
    return render_to_response('oficina.html', locals(), context_instance=RequestContext(request))

def lavajato(request):
    
    banners = Banner.objects.all()
    anuncios = Anunciantes()
    

    return render_to_response('lavajato.html', locals(), context_instance=RequestContext(request))

def localizacao(request):
    
    banners = Banner.objects.all()
    anuncios = Anunciantes()
    
    
    return render_to_response('localizacao.html', locals(), context_instance=RequestContext(request))

def contato(request):
    
    banners = Banner.objects.all()
    anuncios = Anunciantes()
    
    
    if request.method == 'POST':
        form = FormContato(request.POST)
        
        if form.is_valid():
            form.enviar()
            classe = 'sucesso'
            mensagem = 'Mensagem enviada com sucesso!'
            form = FormContato()
        else:
            classe = 'fail'
            mensagem = 'Ocorreu algum erro durante o envio! Tente de novo ou volte mais tarde.'
    else:
        form = FormContato()
    
    return render_to_response('contato.html', locals(), context_instance=RequestContext(request))

def verVeiculos(request, vmarca):
    
    banners = Banner.objects.all()
    anuncios = Anunciantes()
    veiculos = Veiculos.objects.filter(marca = vmarca)
    paginator = Paginator(veiculos, 12)
    
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
        
    try:
        veiculosLista = paginator.page(page)
    except (EmptyPage, InvalidPage):
        veiculosLista = paginator.page(paginator.num_pages)
    
        
    return render_to_response('veiculos.html', locals(), context_instance=RequestContext(request))
        
def verAcessorios(request, tipo_id):
    
    banners = Banner.objects.all()
    acessorios = Acessorio.objects.filter(tipo = tipo_id)
    fotos = FotosAcessorio.objects.all()
    anuncios = Anunciantes()
    paginator = Paginator(acessorios, 12) #mostra 3 acessorios por pagina
    
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
        
    #Se o request estiver fora do limite da pagina, mostra a ultima pagina
    try:
        acessoriosLista = paginator.page(page)
    except (EmptyPage, InvalidPage):
        acessoriosLista =  paginator.page(paginator.num_pages)
    
    
    return render_to_response('acessorios.html', locals(), context_instance=RequestContext(request))

def visualizarAc(request, id_acessorios):
    
    banners = Banner.objects.all()
    anuncios = Anunciantes()
    acessorio = get_object_or_404(Acessorio, pk=id_acessorios)
    foto = FotosAcessorio.objects.filter(acessorio=acessorio)[:1]
    galeria = FotosAcessorio.objects.filter(acessorio=acessorio)
    
    
    if request.method == 'POST':
        formac = FormAcessorio(request.POST)
        
                     
        if formac.is_valid():
            formac.enviar()
            classe = 'Sucesso'
            mensagem = 'Proposta enviada com sucesso, em breve entraremos em contato!'
            formac = FormAcessorio()
            
        else:
            classe = 'fail'
            mensagem = 'Ocorreu um erro ao enviar a proposta. Tente novamente ou volte mais tarde.'
    else:
        formac = FormAcessorio(initial={'acessorio': acessorio.nome, 'marca':acessorio.marca, 'valor':acessorio.valor})
    
    
    return render_to_response('visualizarAc.html', locals(), context_instance=RequestContext(request))

def visualizarVe(request, id_eventos):
    
    banners = Banner.objects.all()
    anuncios = Anunciantes()
    galeriaeventos = Eventos.objects.get(pk = id_eventos)
    
    return render_to_response('visualizarVe.html', locals(), context_instance=RequestContext(request))

def buscaEvento(request):
    
    banners = Banner.objects.all()
    anuncios = Anunciantes()
    
    if request.method == 'POST':
        eventos = Evento.objects.filter(titulo__icontains=request.POST['query']) 
        query = request.POST['query']
    
    
    return render_to_response('buscaevento.html', locals(), context_instance=RequestContext(request))

def visualizarEv(request, evento_id):
    
    banners = Banner.objects.all()
    anuncios = Anunciantes()
    evento = get_object_or_404(Evento, pk=evento_id)
    
    
    
    return render_to_response('visualizarEv.html', locals(), context_instance=RequestContext(request))

def news(request):
    
    banners = Banner.objects.all()
    anuncios = Anunciantes()
    
    
    if request.method == 'POST':
        form = FormNewsletter(request.POST)
        
        if form.is_valid():
            return render_to_response('newsletter.html',locals(), context_instance=RequestContext(request))
    else:
        form = FormNewsletter()
        return render_to_response('newsletter.html',locals(), context_instance=RequestContext(request))

def newsletter(request):
    
    banners = Banner.objects.all()
    anuncios = Anunciantes()
    
    if request.method == 'POST':
        form = FormNewsletter(request.POST)
        
        if form.is_valid():
            return render_to_response('news.html',locals(), context_instance=RequestContext(request))
    else:
        form = FormNewsletter()
        return render_to_response('news.html',locals(), context_instance=RequestContext(request))

def equipe(request):
    
    banners = Banner.objects.all()
    anuncios = Anunciantes()
    
    return render_to_response('equipe.html', locals(), context_instance=RequestContext(request))

def expedicao(request):
    
    banners = Banner.objects.all()
    anuncios = Anunciantes()
    
    return render_to_response('expedicao.html', locals(), context_instance=RequestContext(request))

def dicas(request):
    
    banners = Banner.objects.all()
    anuncios = Anunciantes()
    
    return render_to_response('dicas.html', locals(), context_instance=RequestContext(request))


def visualizarGa(request, id_evento):
    
    banners = Banner.objects.all()
    anuncios = Anunciantes()
    eventos = Eventos.objects.get(pk = id_evento)
    imagens = ImagemGaleria.objects.filter(galeriaEvento = id_evento)
    return render_to_response('visualizarGa.html', locals(), context_instance=RequestContext(request))

def visualizaroutroev(request):
    
    banners = Banner.objects.all()
    anuncios = Anunciantes()
    eventos = Evento.objects.order_by('-id')
    return render_to_response('visualizarOutrosEv.html', locals(), context_instance=RequestContext(request))

def eventosant(request):
    
    banners = Banner.objects.all()
    anuncios = Anunciantes()
      
    capa = ImagemGaleria.objects.filter(capa = 1).order_by('-id')
    
    paginator = Paginator(capa, 12)
    
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
        
    try:
        capaLista = paginator.page(page)
    except (EmptyPage, InvalidPage):
        capaLista = paginator.page(paginator.num_pages)
    
    
    return render_to_response('eventosAnt.html', locals(),  context_instance=RequestContext(request))

def aconteceu(request):
    
    banners = Banner.objects.all()
    anuncios = Anunciantes()
    
    titulosacontecimentos = Aconteceu.objects.all().order_by('-id')
    
    return render_to_response('aconteceu.html', locals(),  context_instance=RequestContext(request))


def veraconteceu(request,id):
    
    banners = Banner.objects.all()
    anuncios = Anunciantes()
    
    titulosacontecimentos = Aconteceu.objects.filter(pk=id )
    conteudoacontecimentos = ConteudoAconteceu.objects.filter(pk = id)
    
    return render_to_response('verAconteceu.html', locals(),  context_instance=RequestContext(request))


