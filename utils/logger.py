# -*- coding: utf-8 -*-

import logging
import os

# Constants for logging
__log_message_format = '%(levelname)s - %(asctime)-10s %(message)s'
__message_format = 'Message "%s" from "%s" with answer "%s"'
__message_log_filename = os.path.join(os.path.dirname(__file__), "../logs/bismark." + __name__.split('.')[0] + ".log")

# Init logging
logging.basicConfig(format=__log_message_format, filename=__message_log_filename, filemode="w", level=logging.DEBUG)


def log_func(is_debug=False):
    r"""
    Decorator for log function name

    :param is_debug: if True write in debug-log, else in info-log
    :return: decorator
    """

    def decorator(func):
        def wrapper(*args, **kwargs):

            if is_debug:
                logging.debug("-" * 3 + ">" + func.__name__ + "()")
            else:
                logging.info("-" * 3 + ">" + func.__name__ + "()")

            return func(*args, **kwargs)

        return wrapper

    return decorator


def class_construct(init):
    r"""
    Decorator for log class init in info-log

    :param init: class __init__
    :return: decorator
    """

    def wrapper(*args, **kwargs):
        logging.info("=>" + args[0].__class__.__name__ + " init")
        init(*args, **kwargs)

    return wrapper


def debug(message):
    r"""
    Write in debug-log

    :param message: message for write
    :return: None
    """

    logging.debug("~" * 5 + ">" + message)


def info(message):
    r"""
    Write in info-log

    :param message: message for write
    :return: None
    """

    logging.info("~" * 5 + ">" + message)


def error(message):
    r"""
    Write in error-log

    :param message: message for write
    :return: None
    """

    logging.error("!" + "-" * 5 + "!" + ">" + message)


def critical(message):
    r"""
    Write in critical-log

    :param message: message for write
    :return: None
    """

    logging.critical("!" * 5 + ">" + message)


def log_message(message, user, answer):
    r"""
    Write bot message for send in info-log

    :param message: user message text
    :param user: user who sent message
    :param answer: bot answer
    :return: None
    """

    logging.info(__message_format % (message, user, answer))
