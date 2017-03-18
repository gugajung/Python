'''
Created on 07/12/2012

@author: User
'''
from django.contrib import admin
from manaia.newsletter.models import Newsletters

class AdminNewsletters(admin.ModelAdmin):
    list_display = ('nome','email')

admin.site.register(Newsletters, AdminNewsletters)