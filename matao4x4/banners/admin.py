from django.contrib import admin
from matao4x4.banners.models import Banner

class BannerAdmin(admin.ModelAdmin):
    list_display = ['imagem']

admin.site.register(Banner, BannerAdmin)