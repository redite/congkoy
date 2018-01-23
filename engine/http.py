# -*- coding: utf-8 -*-
import os
import json
import logging
import logging.config
from flask import Flask
from engine import handler


def initialize():
    """Initialize HTTP Instance

    :rtype: Flask
    """
    def _register_blueprint(flask_app):
        """python bisa punya fungsi di dalam fungsi,
        yang hanya bisa dipanggil dari scope parent function."""
        from modules import home
        flask_app.register_blueprint(home.home)

    server = Flask("Congkoy", instance_relative_config=True)
    server.config.from_object('engine.config.CongkoyConfig')

    #: initialize error handler
    server.register_error_handler(404, handler.not_found_handler)
    server.register_error_handler(Exception, handler.python_exc_handler)  #: core python exception

    #: setup logging
    __setup_logging()

    #: register blueprint
    _register_blueprint(server)

    from werkzeug.contrib.fixers import ProxyFix
    server.wsgi_app = ProxyFix(server.wsgi_app)
    return server


def __setup_logging():
    """setup logging to file"""
    homedir = os.environ['HOME']
    debug = os.environ.get('DEBUG', True)
    version = "devel" if debug else "prod"

    loglocation = os.path.join(
        homedir,
        "logs",
        "congkoy",
        'congkoy_{}.log'.format(version)
    )

    log_dir = os.path.dirname(loglocation)
    if not os.path.exists(log_dir):
        os.mkdir(log_dir)

    base_config = os.path.join(os.path.dirname(__file__), '..', 'etc', 'log_config.json')

    with open(base_config, 'r') as f:
        conf = json.loads(f.read())

    conf['handlers']['file_handler']['filename'] = loglocation
    conf['handlers']['file_handler']['level'] = 'DEBUG' if debug else "WARN"
    conf['handlers']['stream_handler']['level'] = 'DEBUG' if debug else "WARN"

    logging.config.dictConfig(conf)
