"""
WSGI config for config project.

It exposes the WSGI callable as a module-level variable named ``application``.

<<<<<<< HEAD
For more information on this media, see
=======
For more information on this file, see
>>>>>>> aad13fa94ff72271216ee7c415d5cb2ac195f5ef
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_wsgi_application()
