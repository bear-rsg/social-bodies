"""
Settings that are specific to this particular instance of the project.
This can contain sensitive information (such as keys) and should not be shared with others.

REMEMBER: If modfiying the content of this file, reflect the changes in local_settings.example.py
"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Create a SECRET_KEY.
# Online tools can help generate this for you, e.g. https://www.miniwebtool.com/django-secret-key-generator/
SECRET_KEY = ''

# Set to True if in development, or False is in production
DEBUG = True/False

# Set to ['*'] if in development, or specific IP addresses and domains if in production
ALLOWED_HOSTS = ['*']/['social-bodies.bham.ac.uk']

# Set the database name below
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'social-bodies.sqlite3'),
        'TEST': {
            'NAME': os.path.join(BASE_DIR, 'social-bodies_TEST.sqlite3'),
        },
    }
}

# Provide the email address for the site admin (e.g. the researcher/research team)
ADMIN_EMAIL = '...@bham.ac.uk'

# Email settings
if DEBUG is True:
    EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
    EMAIL_FILE_PATH = os.path.join(BASE_DIR, 'sent_emails')
else:
    EMAIL_USE_TLS = False
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = ''
    EMAIL_PORT = 25
EMAIL_HOST_USER = ADMIN_EMAIL
DEFAULT_FROM_EMAIL = ADMIN_EMAIL
NOTIFICATION_EMAIL = (ADMIN_EMAIL,)
