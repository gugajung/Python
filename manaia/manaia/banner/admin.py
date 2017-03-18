'''
Created on 06/12/2012

@author: User
'''
from django.contrib import admin
from manaia.banner.models import Banner
from sorl.thumbnail.admin import AdminImageMixin

class BannerAdmin(AdminImageMixin, admin.ModelAdmin):
    list_filter = ('descricao',)
    search_fields = ('descricao',)
    list_display = ('descricao',)
    

admin.site.register(Banner, BannerAdmin)    