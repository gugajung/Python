from django.db import models

# Create your models here.
class Banner(models.Model):
    imagem = models.ImageField(upload_to='img/banners/')
    
    def __unicode__(self):
        return 'Banner {0}'.format(self.id)