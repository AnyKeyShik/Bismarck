# -*- coding: utf-8 -*-

import datetime
import logging
import os

# Constants for logging
_log_message_format = '%(levelname)s - %(asctime)-10s %(message)s'
_message_format = 'Message "%s" from "%s" with answer "%s"'
_message_log_filename = os.path.join(os.path.dirname(__file__), "../../logs/bismark_" +
                                     datetime.datetime.now().strftime("%Y_%m_%d_%H-%M-%S") + ".log")

# Init logging
logging.basicConfig(format=_log_message_format, filename=_message_log_filename, filemode="w", level=logging.DEBUG)

DEBUG_LOG = True


def log_func(log_write=False):
    """
    Decorator for log function name

    :param log_write: if True write in debug-log, else in info-log
    :return: decorator
    """

    def decorator(func):
        def wrapper(*args, **kwargs):

            if log_write and DEBUG_LOG:
                logging.debug("-" * 3 + ">" + func.__name__ + "()")
            else:
                logging.info("-" * 3 + ">" + func.__name__ + "()")

            return func(*args, **kwargs)

        return wrapper

    return decorator


def class_construct(init):
    """
    Decorator for log class init in info-log

    :param init: class __init__
    :return: decorator
    """

    def wrapper(*args, **kwargs):
        logging.info("=>" + args[0].__class__.__name__ + " init")
        init(*args, **kwargs)

    return wrapper


def debug(tag, message):
    """
    Write in debug-log

    :param tag: tag for logging
    :param message: message for write
    :return: None
    :rtype: None
    """

    if DEBUG_LOG:
        logging.debug(str(tag) + ": " + "~" * 5 + ">" + str(message))


def info(tag, message):
    """
    Write in info-log

    :param tag: tag for logging
    :param message: message for write
    :return: None
    :rtype: None
    """

    logging.info(str(tag) + ": " + "~" * 5 + ">" + str(message))


def warning(tag, message):
    """
    Write in warning-log

    :param tag: tag for logging
    :param message: message for write
    :return: None
    :rtype: None
    """

    logging.warning(str(tag) + ": " + "!" + "-" * 5 + "!" + ">" + str(message))


def error(tag, message):
    """
    Write in error-log

    :param tag: tag for logging
    :param message: message for write
    :return: None
    :rtype: None
    """

    logging.error(str(tag) + ": " + "!" + "-" * 5 + "!" + ">" + str(message))


def critical(tag, message):
    """
    Write in critical-log

    :param tag: tag for logging
    :param message: message for write
    :return: None
    :rtype: None
    """

    logging.critical(str(tag) + ": " + "!" * 5 + ">" + str(message))


def log_message(message, user, answer):
    """
    Write bot message for send in info-log

    :param message: user message text
    :param user: user who sent message
    :param answer: bot answer
    :return: None
    """

    logging.info(_message_format % (message, user, answer))
