import os
from django.conf import settings


DEBUG = False
TEMPLATE_DEBUG = False

SHARE_URL = ['https://serene-beach-9732.herokuapp.com']

DATABASES = settings.DATABASES

# Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES['default'] = dj_database_url.config()
DATABASES['default']['ENGINE'] = 'django_postgrespool'

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Static asset configuration
#import os
#BASE_DIR = os.path.dirname(os.path.abspath(__file__))
#STATIC_ROOT = 'staticfiles'
#STATIC_URL = '/static/'

#STATICFILES_DIRS = (
#    os.path.join(BASE_DIR, 'static'),
#)