# -*- coding: utf-8 -*-

from datetime import date
from django import forms
from django.conf import settings
from django.core import serializers
from django.core.mail import EmailMultiAlternatives
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.db.models.query_utils import Q
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from sincomercio.acoes_sociais.models import AcaoSocial
from sincomercio.arquivos.models import Arquivo
from sincomercio.banners.models import Banner
from sincomercio.campanhas.models import Campanha
from sincomercio.comunicados.models import Comunicado
from sincomercio.contribuicoes.models import Contribuicao, ConteudoContribuicao
from sincomercio.imagens.models import ImagemNoticia, ImagemAcoesSociais, \
    ImagemCampanha
from sincomercio.links.models import Link
from sincomercio.loja_aniver.models import LojaAniver
from sincomercio.noticias.models import Noticia, NoticiasTv
from sincomercio.utils.auxiliares import cria_paginacao
from sincomercio.videoteca.models import Genero, Videoteca
from sincomercio.parceiros.models import Parceiro
from sincomercio.parceiros.flags import Status
from sincomercio.eventos.models import Eventos, GaleriaEvento, ImagemGaleria
from sincomercio.calendario.models import Calendario
from sincomercio.calendarioMercado.models import CalendarioMercado
from sincomercio.palestras.models import Plestras
#from django.core.serializers import serializers

def index(request):
    # 6 ultimas noticias
    noticias_fecomercio = Noticia.objects.filter(status='A',fonte__icontains='Fecom')[0:5]
    noticias = Noticia.objects.filter(status='A').exclude(fonte__icontains='Fecom')[0:5]
    # LISTA APENAS A ULTIMA NOTICIA
    ultimaNoticia = Noticia.objects.filter(status='A')[0:1]
    
    # LISTA DE IMAGEM DA ULTIMA NOTICIA
    imagemUltimaNoticia = ImagemNoticia.objects.filter(noticia=ultimaNoticia)[:1]
    
    # RETORNA OS ULTIMOS 2 VIDEOS INSERIDOS
    videos = Videoteca.objects.filter(status='A')[:2]
    
    # LISTA DE LOJAS ANIVERSARIANTES
#    dia = hoje.split('-')[-1]
#    mes = hoje.split('-')[-2]
    
    lojas_aniver = LojaAniver.objects.filter(data_aniver=date.today())[:1]
    
    
    # ACOES SOCIAIS
    ultima_acao = AcaoSocial.objects.filter(status='A')[:1]
    imagem_acao = ImagemAcoesSociais.objects.filter(acao=ultima_acao)[:1]
    
    #ALBUM
    
    
    

    ultima_campanha = Campanha.objects.filter(status='A')[:1]
    imagem_campanha = ImagemCampanha.objects.filter(campanha=ultima_campanha)[:1]
    
    # BANNERS
    
    # banners do topo lateral direito
    banners_tld = Banner.objects.filter(posicao='tld')
    # banners do meio lateral direito
    banners_mld = Banner.objects.filter(posicao='mld')
    # banners do baixo lateral direito
    banners_bld = Banner.objects.filter(posicao='bld')
    
    estilo = "position: relative; top: 250px;top:0\9;position:none\9;margin-top:-870px\9;"
    
    #noticias tv
    ultima_noticia_tv = NoticiasTv.objects.filter(status='A')[:1]
    data = date.today()
    listaComunicados = Comunicado.getComunicados(data)
    
    #Parceiros
    parceiros = Parceiro.objects.filter(visibilidade = Status.VISIVEL)
    
    #Eventos
    eventos = Eventos.objects.all().order_by("-id")[:1]
    
    return render_to_response('index.html', locals(), context_instance=RequestContext(request))

def quem_somos(request):
#    banners_tld = Banner.objects.filter(posicao='tld')
#    banners_mld = Banner.objects.filter(posicao='mld')
#    banners_bld = Banner.objects.filter(posicao='bld')
    
    estilo = "margin-top: -10px\9;"
    
    return render_to_response('quem_somos.html', locals(), context_instance=RequestContext(request))


def conhecasincomercio(request):

    return render_to_response('conhecasincomercio.html',locals(), context_instance=RequestContext(request))


def servicos(request):
#    banners_tld = Banner.objects.filter(posicao='tld')
#    banners_mld = Banner.objects.filter(posicao='mld')
#    banners_bld = Banner.objects.filter(posicao='bld')
    
    estilo = "margin-top : -10px\9;"
    
    return render_to_response('servicos.html', locals(), context_instance=RequestContext(request))

def campanhas(request):
#    banners_tld = Banner.objects.filter(posicao='tld')
#    banners_mld = Banner.objects.filter(posicao='mld')
#    banners_bld = Banner.objects.filter(posicao='bld')

    lista_campanhas = Campanha.objects.filter(status='A')
    campanhas = cria_paginacao(request, lista_campanhas)
    
    estilo = "margin-top : -170px\9;"
    
    return render_to_response('campanhas.html', locals(), context_instance=RequestContext(request))

class FormContato(forms.Form):
    empresa = forms.CharField(max_length=50, error_messages={'required':'Por favor, digite o nome de sua Empresa'})
    email = forms.EmailField(required=True, 
                             error_messages={'required':'Por favor, digite o seu e-mail', 
                                             'invalid':'Digite um email válido'}
                             )
    telefone = forms.CharField(max_length=13, error_messages={'required': 'Por favor, digite seu telefone'})
    contato = forms.CharField(max_length=100, error_messages={'required':'Por favor, digite o seu contato'})
    mensagem = forms.Field(widget=forms.Textarea, error_messages={'required':'Por favor, digite a sua mensagem'})
    
    def enviar(self):
        titulo = 'SinComércio Matão - Contato do Site'
        destino = 'scvmatao@fecomercio.com.br'
        texto = """
        <html>
        <head>
        <meta http-equiv="Content-Type" content="text/html;charset=utf-8" />
        <style>
            body{font-family:Arial;}
            h2{color: #2d321b;}
            #moldura-msg{width: 500px; height:auto; border: 2px solid green;background:#f9fee8; padding: 10px}
            #moldura-msg #campos-msg{text-align:left;}
            #moldura-msg #campos-msg label{margin-top:10px;width: 150px; display:block; font: bold 12px Arial;}
            #moldura-msg #campos-msg label span {font: normal 12px Arial;}
        </style>
        </head>
        <body>
        <center>
        <img src="http://www.sysnetwork.com.br/teste/sindicato/_off/Logo.jpg" border="0"/>
        <h2>Contato - SinCom&eacute;rcio Mat&atilde;o</h2>
            <div id="moldura-msg">
                <div id="campos-msg">
                    <label for="empresa">
                        Empresa<br />
                        <span>%(empresa)s</span>
                    </label>
                    <label for="email">
                        E-Mail
                        <span>%(email)s</span>
                    </label>
                    <label for="telefone">
                        Telefone
                        <span>%(telefone)s</span>
                    </label>
                    <label for="contato">
                        Contato<br />
                       <span> %(contato)s</span>
                    </label>
                    <label for="mensagem">
                        Mensagem<br/>
                        <span>%(mensagem)s</span>
                    </label>
                </div>
            </div>
        </center>
        </body>
        </html>
        """ % self.cleaned_data
        mail = EmailMultiAlternatives(titulo, '', self.cleaned_data['email'], [destino])
        # ANEXA O TIPO DE DADOS A SER ENVIADO
        mail.attach_alternative(texto, 'text/html')
        mail.send()

def contato(request):
#    banners_tld = Banner.objects.filter(posicao='tld')
#    banners_mld = Banner.objects.filter(posicao='mld')
#    banners_bld = Banner.objects.filter(posicao='bld')
#    
    # se for enviado o form preenchido
    if request.method == 'POST':
        # cria um form com os valores inseridos
        form = FormContato(request.POST)
        
        # verifica se valores do form são válidos
        if form.is_valid():
            # envia o form
            form.enviar()
            # mensagem a ser retorna caso tenha sido enviado
            mostrar = 'Sua mensagem foi enviada! Obrigado!'
    else:
        # retorna um form em branco
        form = FormContato()
    
    estilo = "margin-top : -370px\9;"
    
    return render_to_response(
        'contato.html',
        locals(),
        context_instance=RequestContext(request)                          
    )
        

def localizacao(request):
#    banners_tld = Banner.objects.filter(posicao='tld')
#    banners_mld = Banner.objects.filter(posicao='mld')
#    banners_bld = Banner.objects.filter(posicao='bld')
    
    estilo = "margin-top: -370px\9;"
    
    return render_to_response('localizacao.html', locals(), context_instance=RequestContext(request))

def videoteca(request):
#    banners_tld = Banner.objects.filter(posicao='tld')
#    banners_mld = Banner.objects.filter(posicao='mld')
#    banners_bld = Banner.objects.filter(posicao='bld')
    
    q = request.GET.get("genero")
    
    if q:
        if q == "0":
            lista_filmes = Videoteca.objects.filter(status='A').all().order_by('-id')
        else:
            lista_filmes = Videoteca.objects.filter(genero=q)
            genero = Genero.objects.filter(id=q)
            for gen in genero:
                genero_nome = gen.nome
    else:
        lista_filmes = Videoteca.objects.filter(status='A').all().order_by('-id')
            
    filmes = cria_paginacao(request, lista_filmes)
    lista_generos = Genero.objects.all().order_by('-id')

    estilo = "margin-top: -150px\9;"

    return render_to_response('videoteca.html', locals(), context_instance=RequestContext(request))

def lojas(request):
#    banners_tld = Banner.objects.filter(posicao='tld')
#    banners_mld = Banner.objects.filter(posicao='mld')
#    banners_bld = Banner.objects.filter(posicao='bld')
    
    lista_lojas = LojaAniver.objects.all().order_by('data_aniver',)
    lojas = cria_paginacao(request, lista_lojas)
    estilo = "margin-top: -90px\9;"
              
    return render_to_response('lista_lojas.html', locals(), context_instance=RequestContext(request))

def noticias(request, fonte):
    
    # BANNERS
#    banners_tld = Banner.objects.filter(posicao='tld')
#    banners_mld = Banner.objects.filter(posicao='mld')
#    banners_bld = Banner.objects.filter(posicao='bld')
    
    if fonte == 'todas':
        lista_noticias = Noticia.objects.filter(status='A')
    elif fonte == 'tv':
        lista_noticias = NoticiasTv.objects.filter(status='A')
    else:
        lista_noticias = Noticia.objects.filter(status='A', fonte=fonte)
        
    noticias = cria_paginacao(request, lista_noticias)
        
    estilo = "margin-top: -230px\9;" 
    
    return render_to_response('lista_noticias.html', locals(),context_instance=RequestContext(request))
    
def acoes_sociais(request):
#    banners_tld = Banner.objects.filter(posicao='tld')
#    banners_mld = Banner.objects.filter(posicao='mld')
#    banners_bld = Banner.objects.filter(posicao='bld')

    lista_acoes = AcaoSocial.objects.filter(status='A')
    acoes = cria_paginacao(request, lista_acoes)
    
    return render_to_response('lista_acoes.html', locals(),context_instance=RequestContext(request))

def busca(request):
    
    q = request.GET.get("busca")
        
    if q:            
        lista_noticias = Noticia.objects.filter(titulo__icontains=q)
        noticias = cria_paginacao(request, lista_noticias)
    else:
        redirect("/busca/?busca=")
            
#    banners_tld = Banner.objects.filter(posicao='tld')
#    banners_mld = Banner.objects.filter(posicao='mld')
#    banners_bld = Banner.objects.filter(posicao='bld')
    
#    estilo = "top: -50px;"    
    
    return render_to_response("busca.html", locals(), context_instance=RequestContext(request))

def links(request):
    lista_links = Link.objects.all()
    links = cria_paginacao(request, lista_links)
    return render_to_response('links.html',locals(),context_instance=RequestContext(request))

def calendario(request):
    datas = Calendario.objects.all(); 
    calendarios = Arquivo.objects.filter(categoria = 2).all().order_by('-ano')
    return render_to_response('calendario.html',locals(), context_instance=RequestContext(request))

def calendarioMercado(request):
    datas = CalendarioMercado.objects.all(); 
    calendariosSuper = Arquivo.objects.filter(categoria = 4).all().order_by('-ano')
    return render_to_response('calendariomercado.html',locals(), context_instance=RequestContext(request))

def acordo(request):
#    banners_tld = Banner.objects.filter(posicao='tld')
#    banners_mld = Banner.objects.filter(posicao='mld')
#    banners_bld = Banner.objects.filter(posicao='bld')

    acordo=acordo =Arquivo.objects.filter(categoria = 1).all().order_by('-ano')
    
    return render_to_response('acordo.html', locals(), context_instance=RequestContext(request))


def motorista(request):
    
    motorista= Arquivo.objects.filter(categoria = 3).all().order_by('-id')
    
    return render_to_response('motorista.html', locals(), context_instance=RequestContext(request))

def inauguracao(request):
#    banners_tld = Banner.objects.filter(posicao='tld')
#    banners_mld = Banner.objects.filter(posicao='mld')
#    banners_bld = Banner.objects.filter(posicao='bld')
    return render_to_response('inauguracao.html',locals(),context_instance=RequestContext(request))

def getXML(request):
    import urllib2
    xml = urllib2.urlopen('http://www.fecomercio.com.br/rss/').read()
    return HttpResponse(xml, 'text/xml')

def info_video(request,id):
    if(request.method=='GET'):
        info = Videoteca.objects.get(pk=id)
        json= serializers.serialize("json",info)
        return HttpResponse(json,"aplication/json")
        
def repis(request):
    
    return render_to_response('repis.html',locals(),context_instance=RequestContext(request))       
 
def contribuicao(request):
    
    contribuicao = Contribuicao.objects.filter(status='A').all().order_by('id')
    
    return render_to_response('contribuicao.html',locals(),context_instance=RequestContext(request))       

def lercontribuicao(request, id):
    contribuicao = Contribuicao.objects.filter(pk=id )
    listacontribuicao = ConteudoContribuicao.objects.filter(categoria = id)
    
    return render_to_response('ler_contribuicao.html',locals(),context_instance=RequestContext(request))

def eventos(request,id):
    evento = Eventos.objects.get(pk = id)
    imagens = ImagemGaleria.objects.filter(galeriaEvento__evento = id)
    return render_to_response('eventos.html',locals(),context_instance=RequestContext(request))

def evento(request):
    eventos = Eventos.objects.all()
    paginator = Paginator(eventos, 1)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    
    try:
        fp = paginator.page(page)
    except (EmptyPage, InvalidPage):
        fp = paginator.page(paginator.num_pages)
    return render_to_response('evento.html',locals(),context_instance=RequestContext(request))
def tipocontribuicao(request):
    
    return render_to_response('contribuicoestipos.html',locals(),context_instance=RequestContext(request))

def palestras(request):
    palestras = Plestras.objects.filter(data__gte =date.today()).order_by('data');
    
    return render_to_response('lista_palestras.html', locals(),
            context_instance=RequestContext(request))
    
def palestra(request,id):
    palestras = Plestras.objects.filter(pk = id)
    return render_to_response('detalhepalestra.html',locals(),context_instance=RequestContext(request))
