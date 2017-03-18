'''
Created on 24/09/2012

@author: Jonatas
'''
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from Montejato.forms import  FormContato

def index(request):
    
    return render_to_response('content.html', locals(), context_instance=RequestContext(request))

def Jateamento(request):
    
    return render_to_response('home/jateamento.html', locals(), context_instance=RequestContext(request))

def Construcao(request):
    
    return render_to_response('home/construcao.html', locals(), context_instance=RequestContext(request))

def Montagem(request):
    
    return render_to_response('home/montagem.html', locals(), context_instance=RequestContext(request))

def Contato(request):
    
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

def Parceiros(request):
    
    return render_to_response('parceiros.html', locals(), context_instance=RequestContext(request))

def Servicos(request):
    
    return render_to_response('servicos.html', locals(), context_instance=RequestContext(request))

def Empresa(request):
    
    return render_to_response('empresa.html', locals(), context_instance=RequestContext(request))