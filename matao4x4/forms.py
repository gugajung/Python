#-*- coding: utf-8 -*-

from django import forms
from django.core.mail.message import EmailMultiAlternatives
from django.contrib.localflavor.br.forms import BRPhoneNumberField

class FormContato(forms.Form):
    nome = forms.CharField(max_length=120)
    telefone = BRPhoneNumberField(required=False)
    cidade = forms.CharField(max_length=40, required=False)
    email = forms.CharField(max_length=120)
    mensagem = forms.CharField(widget=forms.Textarea(attrs={'rows':7, 'cols':32}))
    
    def enviar(self):
        titulo = 'Fale Conosco - [Matao 4x4]'
        destino = 'matao4x4@matao4x4.com.br'
        texto = u"""
                   <html>
                       <head>
            <meta http-equiv="Content-Type" content="text/html;charset=utf-8" />
            <style>
                body{font-family:Arial;}
                h2{color: #ffa70e;}
                #moldura-msg{width: 500px; height:auto; border: 2px solid #ec9703;background:#fff; padding: 10px}
                #moldura-msg #campos-msg{text-align:left;}
                #moldura-msg #campos-msg label{margin-top:10px;width: 150px; display:block; font: 12px Arial;}
                #moldura-msg #campos-msg label span {font: normal 12px Arial;}
            </style>
            </head>
            <body>
            <center>
            <h2>Contato - Matão 4x4</h2>
                <div id="moldura-msg">
                    <div id="campos-msg">
                        <label for="empresa">
                            <b>Nome: </b>
                            <span>%(nome)s<br/></span>
                            <b>Telefone: </b> <span>%(telefone)s</span><br/>
                            <b>Cidade: </b> <span>%(cidade)s</span><br/>
                        </label>
                        <label for="email">
                            <b>E-Mail: </b>
                            <span>%(email)s<br/></span>
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
                
        mail = EmailMultiAlternatives(titulo, texto, self.cleaned_data['email'], [destino,])
        mail.attach_alternative(texto, 'text/html')
        mail.send()
        
        
class FormAcessorio(forms.Form):
    nome = forms.CharField(max_length=120, required=True)
    email = forms.EmailField(max_length=130, required=True)
    telefone = BRPhoneNumberField()
    mensagem = forms.CharField(widget=forms.Textarea(attrs={'rows':7, 'cols':32}))
    acessorio = forms.CharField(widget=forms.HiddenInput, max_length=255, required=False)
    marca = forms.CharField(widget=forms.HiddenInput, max_length=255, required=False)
    valor = forms.CharField(widget=forms.HiddenInput, required=False)
    
    def enviar(self):
        
        titulo = "Acessorios - [Matao 4x4]"
        destino = "matao4x4@matao4x4.com.br"
        texto = u"""
                <html>
                    <head>
                        <meta http-equiv="Content-Type" content="text/html;charset=utf-8" />
                        <style>
                            body {font-family: Arial;}
                            h2 {color: #ffa70e;}
                            #moldura-msg {width: 500px; height: auto; border: 2px solid #ec9703; background: #fff; padding: 10px;}
                            #moldura-msg #campo-msg {text-align: left;}
                            #moldura-msg #campo-msg label {margin-top:10px;width: 505px; display:block; font: 12px Arial;}
                            #moldura-msg #campos-msg label span {12px Arial;}
                        </style>
                    </head>
                    <body>
                        <center>
                            <p>Você recebeu uma nova proposta de negociação!</p>
                            <h2>Acessórios - Proposta [Matão 4x4]</h2>
                            <div id="moldura-msg">
                                <div id="campo-msg">
                                    <label for="acessorio">
                                        <b>Acessório a ser negociado:</b>
                                        <span>%(acessorio)s</span><br/>
                                        <b>Marca: </b>
                                        <span>%(marca)s</span><br/>
                                        <b>Valor: </b>
                                        <span>R$ %(valor)s</span><br/>
                                    </label>
                                    <label for="cliente">
                                        <b>Interessado:</b><br/>
                                        <b>Nome: </b>
                                        <span>%(nome)s</span><br/>
                                        <b>E-mail: </b>
                                        <span>%(email)s</span><br/>
                                        <b>Telefone: </b>
                                        <span>%(telefone)s</span><br/>
                                        <b>Mensagem(observações)</b>
                                        <span>%(mensagem)s</span>
                                    </label>
                                </div>
                            </div>
                        </center>
                    </body>
                </html>
                """ % self.cleaned_data
                
        mail = EmailMultiAlternatives(titulo, texto, self.cleaned_data['email'], [destino,])
        mail.attach_alternative(texto, 'text/html')
        mail.send()
        

class FormVeiculo(forms.Form):
    nome = forms.CharField(max_length=120, required=True)
    email = forms.EmailField(max_length=130, required=True)
    telefone = BRPhoneNumberField(required=False)
    mensagem = forms.CharField(widget=forms.Textarea(attrs={'rows':7, 'cols':32}))
    modelo = forms.CharField(widget=forms.HiddenInput, max_length=255, required=False)
    marca = forms.CharField(widget=forms.HiddenInput, max_length=255, required=False)
    valor = forms.FloatField(widget=forms.HiddenInput, required=False)
    newsletter = forms.BooleanField(widget=forms.CheckboxInput(), required=False)
    
    def enviar(self):
        titulo = "Veiculos - [Matao 4x4]"
        destino = "matao4x4@matao4x4.com.br"
        texto = u"""
                <html>
                    <head>
                        <meta http-equiv="Content-Type" content="text/html;charset=utf-8" />
                        <style>
                            body {font-family: Arial;}
                            h2 {color: #ffa70e;}
                            #moldura-msg {width: 500px; height: auto; border: 2px solid #ec9703; background: #fff; padding: 10px;}
                            #moldura-msg #campo-msg {text-align: left;}
                            #moldura-msg #campo-msg label {margin-top:10px;width: 505px; display:block; font: 12px Arial;}
                            #moldura-msg #campos-msg label span {12px Arial;}
                        </style>
                    </head>
                    <body>
                        <center>
                            <p>Você recebeu uma nova proposta de negociação!</p>
                            <h2>Veículo - Proposta [Matão 4x4]</h2>
                            <div id="moldura-msg">
                                <div id="campo-msg">
                                    <label for="veiculo">
                                        <b>Veículo a ser negociado:</b>
                                        <span>%(modelo)s</span><br/>
                                        <b>Marca: </b>
                                        <span>%(marca)s</span><br/>
                                        <b>Valor: </b>
                                        <span>R$ %(valor)s</span><br/>
                                    </label>
                                    <label for="cliente">
                                        <b>Interessado:</b><br/>
                                        <b>Nome: </b>
                                        <span>%(nome)s</span><br/>
                                        <b>E-mail: </b>
                                        <span>%(email)s</span><br/>
                                        <b>Telefone: </b>
                                        <span>%(telefone)s</span><br/>
                                        <b>Mensagem(observações)</b>
                                        <span>%(mensagem)s</span>
                                    </label>
                                </div>
                            </div>
                        </center>
                    </body>
                </html>
                """ % self.cleaned_data
                
        mail = EmailMultiAlternatives(titulo, texto, self.cleaned_data['email'], [destino,])
        mail.attach_alternative(texto, 'text/html')
        mail.send()

class FormNewsletter(forms.Form):
    nome = forms.CharField(max_length=100)
    email = forms.CharField(max_length=140)
    cidade = forms.CharField(max_length=100, required=False)
    estado = forms.CharField(max_length=75, required=False)