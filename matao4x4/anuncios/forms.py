#-*- coding: utf-8 -*-
from django.core.files.images import get_image_dimensions
from matao4x4.anuncios.models import Anunciante
from django import forms

class AnunciantesAdminForm(forms.ModelForm):
        class Meta:
            model = Anunciante

            # validando o campo específico: imagem
            def clean_imagem(self):
                # pego a imagem enviada pelo usuário
                imagem = self.cleaned_data.get("imagem")

                # a imagem não foi enviada?
                if not imagem:
                    # chamo um erro de validação do form
                    raise forms.ValidationError("Você esqueceu de enviar o banner!")
                # se a imagem foi enviada
                else:
                    # pego a largura e altura da imagem
                    largura = get_image_dimensions(imagem)[0]

                # a largura é diferente do padrão?
                if largura != 224:
                    # chamo o erro de validação do form, informando largura e altura necessárias
                    raise forms.ValidationError("A largura da imagem enviada é de %ipx. O correto é 224px." % largura)
                return imagem