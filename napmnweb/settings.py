"""
Django settings for napmnweb project.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from pathlib import Path

from settings_base import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: Replace the SECRET_KEY in production
SECRET_KEY = '-!bhp5em1hk10%k&$kq$#3@u_mj*dqsn9=9v2&e6+t_p6-g-0t'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
    'napmn.webfactional.com',
    '.napmn.com'
	
]

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'appdata',
        'USER': 'napmncom_control',
        'PASSWORD': 'LKz(c*!pT2sk',
        'HOST': '',
        'PORT': '',
        'OPTIONS': {
            'init_command': 'SET storage_engine=INNODB',
        },
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = 'https://napmn.com/static/'

STATIC_ROOT = os.path.join(BASE_DIR,'../../static/')

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

SESSION_EXPIRE_AT_BROWSER_CLOSE=True


