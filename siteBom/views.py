# -*- coding: utf-8 -*-
'''
Created on 03/08/2010

@author: Matheus
'''

from django import forms
from django.core.mail import send_mail
from django.core.mail.message import EmailMultiAlternatives
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.forms.util import ErrorList
from django.shortcuts import render_to_response
from django.template import RequestContext
from siteBom.enquetes.models import Enquete


def index(request):
    ultima_enquete = Enquete.objects.order_by('-data')[:1]
    return render_to_response('index.html', locals(), context_instance=RequestContext(request))

def sobre(request):
    return render_to_response('sobre-a-bom.html', context_instance=RequestContext(request))

class FormContato(forms.Form):
    nome = forms.CharField(max_length=50, error_messages={'required':'Por favor, digite o seu nome'})
    email = forms.EmailField(required=True,
                             error_messages={'required':'Por favor, digite o seu e-mail',
                                             'invalid':'Digite um email válido'}
                             )
    assunto = forms.CharField(max_length=100, error_messages={'required':'Por favor, digite o seu assunto'})
    mensagem = forms.Field(widget=forms.Textarea, error_messages={'required':'Por favor, digite a sua mensagem'})
    
    def enviar(self):
        titulo, destino, texto = 'B.O.M - Contato do Site', 'bombeneficios@uol.com.br', """
        <html>
        <head>
        <meta http-equiv="Content-Type" content="text/html;charset=utf-8" />
        <style type="text/css">
            body{font-family:Arial;}
            h2{color: #2d321b;}
            #moldura-msg{width: 500px; height:auto; border: 2px solid #3e4095;background:#eee; padding: 10px}
            #moldura-msg #campos-msg{text-align:left;}
            #moldura-msg #campos-msg label{margin-top:10px;width: 150px; display:block; font: bold 12px Arial;}
            #moldura-msg #campos-msg label span {font: normal 12px Arial;}
        </style>
        </head>
        <body>
        <center>
        <h2>Contato - B.O.M</h2>
            <div id="moldura-msg">
                <div id="campos-msg">
                    <label for="nome">
                        Nome<br />
                        <span>%(nome)s</span>
                    </label>
                    <label for="email">
                        E-Mail
                        <span>%(email)s</span>
                    </label>
                    <label for="assunto">
                        Assunto<br />
                       <span> %(assunto)s</span>
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
        #ANEXA O TIPO DE DADOS A SER ENVIADO
        mail.attach_alternative(texto, 'text/html')
        mail.send()
       # send_mail(titulo, texto, self.cleaned_data['email'], [destino])

def faleConosco(request):
    
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
    
    return render_to_response(
        'fale-conosco.html',
        locals(),
        context_instance=RequestContext(request)                          
    )

def redeCred(request):
    return render_to_response('rede-credenciada.html', context_instance=RequestContext(request))

def localizacao(request):
    return render_to_response('localizacao.html', context_instance=RequestContext(request))
