# -*- coding: utf-8 -*-

#   Copyright (c) 2020.
#  #
#   Created by AnyKeyShik Rarity
#  #
#   Telegram: @AnyKeyShik
#   GitHub: https://github.com/AnyKeyShik
#   E-mail: nikitag594@gmail.com

#   Copyright (c) 2020.
#  #
#   Created by AnyKeyShik Rarity
#  #
#   Telegram: @AnyKeyShik
#   GitHub: https://github.com/AnyKeyShik
#   E-mail: nikitag594@gmail.com

import logging


class Logger(object):
    def __init__(self, module_name='root'):
        self._logger = logging.getLogger(module_name)
        self._message_format = 'Message "%s" from "%s" with answer "%s"'

    def log_func(self, func):
        """
        Decorator for log function name
        :return: decorator
        """

        def wrapper(*args, **kwargs):
            self._logger.info("|" + "-" * 2 + ">" + func.__name__ + "()")
            return func(*args, **kwargs)

        return wrapper

    def class_construct(self, init):
        """
        Decorator for log class init in info-log

        :param init: class __init__
        :return: decorator
        """

        def wrapper(*args, **kwargs):
            self._logger.info("=>" + args[0].__class__.__name__ + " init")
            init(*args, **kwargs)

        return wrapper

    def debug(self, message):
        """
        Write in debug-log

        :param message: message for write
        :return: None
        :rtype: None
        """

        self._logger.debug("|" + "~" * 5 + ">" + str(message))

    def info(self, message):
        """
        Write in info-log

        :param message: message for write
        :return: None
        :rtype: None
        """

        self._logger.info("|" + "~" * 5 + ">" + str(message))

    def warning(self, message):
        """
        Write in warning-log

        :param message: message for write
        :return: None
        :rtype: None
        """

        self._logger.warning("|" + "~" * 5 + ">" + str(message))

    def error(self, message):
        """
        Write in error-log

        :param message: message for write
        :return: None
        :rtype: None
        """

        self._logger.error("|" + "~" * 5 + ">" + str(message))

    def critical(self, message):
        """
        Write in critical-log

        :param message: message for write
        :return: None
        :rtype: None
        """

        self._logger.critical("|" + "~" * 5 + ">" + str(message))

    def log_message(self, message, user, answer):
        """
        Write bot message for send in info-log

        :param message: user message text
        :param user: user who sent message
        :param answer: bot answer
        :return: None
        """

        self._logger.info(self._message_format % (message, user, answer))
