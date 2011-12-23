'''
Put your production settings here.
The idea is to set your settings to settings.production in production.
This allows you to overwrite anything in common.py
'''
import os
from common import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    "default": {
        "ENGINE": "", # Add "postgresql_psycopg2", "postgresql", "mysql", "sqlite3" or "oracle".
        "NAME": "",                       # Or path to database file if using sqlite3.
        "USER": "",                             # Not used with sqlite3.
        "PASSWORD": "",                         # Not used with sqlite3.
        "HOST": "",                             # Set to empty string for localhost. Not used with sqlite3.
        "PORT": "",                             # Set to empty string for default. Not used with sqlite3.
    }
}

# local_settings.py can be used to override environment-specific settings
# like database and email that differ between development and production.
try:
    from local_settings import *
except ImportError:
    pass
