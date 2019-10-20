"""
WSGI config for VooEatsRest project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application



os.environ['SECRET_KEY']='this_is_my_secret_key'
os.environ['DEBUG']='True'
os.environ['DATABASES_ENGINE']='django.db.backends.postgresql_psycopg2'
os.environ['DATABASES_NAME']='vooeats'
os.environ['DATABASES_USER']='mkrnaqeebi'
os.environ['DATABASES_PASSWORD']='Kamran!12754'
os.environ['DATABASES_HOST']='35.234.219.25'
os.environ['DATABASES_PORT']='5432'
os.environ['FRONT_HOST']='https://vooeats.com'


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "VooEatsRest.settings")

application = get_wsgi_application()
