"""
Settings that are specific to this particular instance of the project.
This can contain sensitive information (such as keys) and should not be shared with others.

REMEMBER: If modfiying the content of this file, reflect the changes in local_settings.example.py
"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'u6n(9&8g-3=6d1#jyp^#))you-h&y^-5y7*&hu)cpxzeu_7#j+'

DEBUG = True

ALLOWED_HOSTS = ['*']

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
