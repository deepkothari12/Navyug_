"""
ASGI config for Navyug_main project.

# It exposes the ASGI callable as a module-level variable named ``application``.

# For more information on this file, see
# https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
# """

# import os

# from django.core.asgi import get_asgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Navyug_main.settings')

# application = get_asgi_application()

import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Navyug_main.settings')

django_app = get_asgi_application()

# Vercel requires the callable to be named "app" or "handler"
app = django_app
handler = django_app
