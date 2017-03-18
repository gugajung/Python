'''
Created on 04/07/2011

@author: SYSNETWORK
'''
import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'manaia.settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()

sys.path.append("/usr/local/www/sysnetwork/testes/django/manaia/")
