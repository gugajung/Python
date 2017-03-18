# -*- coding: utf-8 -*-
from django.conf import settings
from django.template.defaultfilters import slugify

def slug_pre_save(signal, instance, sender, **kwargs):
    """Este signal gera um slug automaticamente. Ele verifica se ja existe um
    objeto com o mesmo slug e acrescenta um numero ao final para evitar
    duplicidade"""
    if not instance.slug:
        slug = slugify(instance.titulo)
        novo_slug = slug
    else:
        novo_slug = slugify(instance.titulo)
    
    contador = 0

    while sender.objects.filter(slug=novo_slug).exclude(id=instance.id).count() > 0:
        contador += 1
        novo_slug = '%s-%d' % (novo_slug, contador)

    instance.slug = novo_slug
        