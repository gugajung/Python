'''
Created on 08/10/2012

@author: Jonatas
'''
#coding: utf-8
from django import forms
from django.core.mail.message import EmailMultiAlternatives


class FormContato(forms.Form):
    nome = forms.CharField(max_length=100,error_messages={'required':'Por favor, digite o seu nome'})
    email = forms.EmailField(required=True,error_messages={'required':'Por favor, digite o seu email'})
    telefone = forms.CharField(required=False, max_length=15)
    assunto = forms.CharField(required=False, max_length=100)
    mensagem = forms.Field(widget=forms.Textarea(attrs={'cols': 38, 'rows': 5}))
    
    def enviar(self):   
        titulo = 'Fale conosco - MonteJato'
        destino = 'jonatas@sysnetwork.com.br'
        
        texto = u"""
            <html>
            <head>
            <meta http-equiv="Content-Type" content="text/html;charset=utf-8" />
            <style>
                body{font-family:Arial;}
                h2{color: #b2ef80;}
                #moldura-msg{width: 500px; height:auto; border: 2px solid #ccc;background:#fff; padding: 10px}
                #moldura-msg #campos-msg{text-align:left;}
                #moldura-msg #campos-msg label{margin-top:10px;width: 150px; display:block; font: bold 12px Arial;}
                #moldura-msg #campos-msg label span {font: normal 12px Arial;}
            </style>
            </head>
            <body>
            <center>
            <h2>Contato - MonteJato</h2>
                <div id="moldura-msg">
                    <div id="campos-msg">
                        <label for="contato"><br />
                            <b>Nome:</b>
                            <span>%(nome)s</span>
                        </label>
                        <label for="email"><br>
                            <b>E-mail:</b>
                            <span>%(email)s</span>
                        </label>
                        <label for="telefone"><br>
                            <b>Telefone: </b>
                            <span>%(telefone)s</span>
                        </label>
                        <label for="assunto"><br>
                            <b>Assunto:</b>
                            <span>%(assunto)s<br/></span>
                        </label>
                        <label for="mensagem">
                            <b>Mensagem:</b><br/>
                            %(mensagem)s
                        </label>
                    </div>
                </div>
            </center>
            </body>
            </html> 
                """ % self.cleaned_data
                
                
        mail = EmailMultiAlternatives(titulo,texto, self.cleaned_data['email'],[destino])  
        mail.attach_alternative(texto, 'text/html')
        mail.send()
        
        