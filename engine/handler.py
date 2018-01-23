# -*- coding: utf-8 -*-
import logging
from flask import jsonify

log = logging.getLogger(__name__)



def not_found_handler(error):
    log.error("not found handler: {}".format(str(error)))
    log.exception(error)

    response = jsonify({
        'message': 'ENODATA',
        'code': 61
    })
    response.status_code = 404
    return response


def python_exc_handler(error):
    """handle native python exception

    :type error: Exception
    :return:
    """
    response = {
        'message': "internal server error",
        'code': 500
    }

    log.error("python exc handler: {}".format(str(error)))
    log.exception(error)

    response = jsonify(response)
    response.status_code = 500
    return response