# -*- coding: utf-8 -*-
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv(), override=True)


MONGODB_HOST = os.environ.get('MONGODB_HOST', '127.0.0.1')
MONGODB_PORT = int(os.environ.get('MONGODB_PORT', 27017))
MONGODB_DBNAME = os.environ.get('MONGODB_DBNAME', 'congkoy')
MONGODB_USERNAME = os.environ.get('MONGODB_USERNAME', 'root')
MONGODB_PASSWORD = os.environ.get('MONGODB_PASSWORD', 'secret')
MONGODB_USE_AUTH = bool(os.environ.get('MONGODB_USE_AUTH', False))


class CongkoyConfig(object):

    #: flask
    DEBUG = os.getenv('DEBUG', 'False')
    if DEBUG.lower() in ['true', '1', 'yes']:
        DEBUG = True

    PORT = int(os.environ.get('PORT', 8008))

    SECRET_KEY = 'supersecret key'

    JSON_AS_ASCII = False
    JSON_SORT_KEYS = False