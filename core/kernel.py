# -*- coding: utf-8 -*-

#   Copyright (c) 2020.
#  #
#   Created by AnyKeyShik Rarity
#  #
#   Telegram: @AnyKeyShik
#   GitHub: https://github.com/AnyKeyShik
#   E-mail: nikitag594@gmail.com

from core.command_processor import CommandProcessor
from core.text_processor import TreeProcessor
from . import logger


class Kernel(object):
    _tree_processor = None
    _command_handler = None

    @logger.class_construct
    def __init__(self):
        self._tree_processor = TreeProcessor()
        self._command_handler = CommandProcessor()

    # @log_func
    def talk(self, message, from_user):
        """
        Main function what send requests to the processors

        :param message: message from user
        :param from_user: is message from private chat with user
        :return: list of answer for user and filename or answer only
        :rtype: list
        """

        self._tree_processor.create_message_tree(message)
        self._tree_processor.parse_message_tree()

        (msg_command, msg_args) = self._tree_processor.get_commands()

        if msg_command == "":
            msg_tags = self._tree_processor.get_tags()
            msg_rating = self._tree_processor.get_rating()

            result = self._command_handler.execute(msg_command, [msg_tags, msg_rating, from_user])
        else:
            result = self._command_handler.execute(msg_command, msg_args)

        return result
