"""
WSGI config for Navyug_main project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Navyug_main.settings')

application = get_wsgi_application()

## we used app beacuse in vercel we need app 
app = application