'''
Created on 16/08/2010

@author: SYSNETWORK
'''
import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'sincomercio.settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()

sys.path.append("/usr/local/www/sysnetwork/testes/django/")
