from django.db import models
from django.db.models import signals
import zipfile
import os
import shutil
from sincomercio.settings import MEDIA_URL, MEDIA_ROOT
from sorl.thumbnail.fields import ImageField
import md5
from zipfile import ZipFile


class Eventos(models.Model):
    class Meta:
        ordering = ('titulo',)
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"

    titulo = models.CharField('Titulo', blank=True, max_length=100)
    sobre = models.TextField('Sobre', blank=True, max_length=100)
    Chamada = models.CharField('Chamada', blank=True, max_length=100)
    data = models.DateField();

    def __unicode__(self):
        return self.titulo
    

class GaleriaEvento(models.Model):

    evento = models.ForeignKey('Eventos')
    file = models.FileField('Arquivo',upload_to='img/galeria',blank=True,null=True, help_text='Apenas Arquivos .zip')

    def __unicode__(self):
        return 'Galeria ' + self.evento.titulo

class ImagemGaleria(models.Model):
    
    galeriaEvento = models.ForeignKey('GaleriaEvento', related_name='imagens')
    imagem = ImageField(upload_to="img/galeria")
    legenda =  models.CharField('Titulo', blank=True, max_length=200)

    def __unicode__(self):
        return "{0} - Imagem da Galeria {1}".format(self.pk,self.galeriaEvento.evento.titulo)
    
    
def acao_post_save(signal, instance, sender, **kwargs):

    if((not instance.file == None) and (not instance.file == "")):
        if(zipfile.is_zipfile(instance.file)):
            file = zipfile.ZipFile(instance.file)
            pasta = os.path.join(os.path.join(MEDIA_ROOT, 'img/galeria'),str(instance.pk))
            if not os.path.exists(pasta):
                os.mkdir(os.path.join(os.path.join(MEDIA_ROOT, 'img/galeria'),str(instance.pk)))
            file.extractall(pasta)
            for imagem in file.infolist():
                novoNome = imagem.filename.replace(imagem.filename[:-4],md5.md5(imagem.filename[:-4]).hexdigest())
                imagemGaleria = ImagemGaleria()
                imagemGaleria.galeriaEvento = instance
#                imagemGaleria.legenda = imagem.filename.replace('jpg','')    
                imagemGaleria.legenda = imagem.filename.split(".")[0]
                imagemGaleria.imagem = os.path.join(pasta,novoNome)
                imagemGaleria.save()
                os.rename(os.path.join(pasta,imagem.filename),os.path.join(pasta,novoNome))
            caminho = os.path.join(MEDIA_ROOT, 'img/galeria/')
            galeria = GaleriaEvento.objects.get(pk = instance.pk)
            galeria.file = None;
            galeria.save()
            for i in os.listdir(caminho):
                print i +"="+ instance.file.name.split('/')[-1]
                if((i[-4:] == ".zip") and (not i == instance.file.name.split('/')[-1])):
                    os.remove(caminho + i)
        

def acao_pre_delete(signal, instance, sender, **kwargs):

    pasta = os.path.join(os.path.join(MEDIA_ROOT, 'img/galeria'),str(instance.pk))
    imagens = ImagemGaleria.objects.filter(galeriaEvento = instance.pk).delete()
    for i in os.listdir(pasta):
        print pasta + i
        os.remove(pasta+ "/" + i)
    os.removedirs(pasta)

    
        
signals.post_save.connect(acao_post_save, sender=GaleriaEvento)
signals.pre_delete.connect(acao_pre_delete, sender=GaleriaEvento)
