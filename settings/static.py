from decouple import config
from .base import BASE_DIR

# URLs to media and static files
STATIC_URL = config('STATIC_URL', default='/static/', cast=str)
MEDIA_URL = config('MEDIA_URL', default='/media/', cast=str)

# Directories to save media and compiled static files
MEDIA_ROOT = BASE_DIR.child('public', 'media')
STATIC_ROOT = BASE_DIR.child('public', 'static')

# Directories to find static files
STATICFILES_DIRS = [
    BASE_DIR.child('webapp', 'static'),
]