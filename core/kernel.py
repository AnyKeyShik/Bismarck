# -*- coding: utf-8 -*-

from core import CommandProcessor
from core import TreeProcessor
from utils.logger import *
from utils.proxy import patch


class Kernel(object):
    _msg = None
    _msg_command = None
    _msg_arguments = None
    _msg_tags = None
    _msg_rating = None

    _tree_parser = None
    _command_handler = None

    @class_construct
    def __init__(self):
        self._tree_parser = TreeProcessor()
        self._command_handler = CommandProcessor()

    def talk(self):
        while 1:
            print(">", end=" ")
            self._msg = str(input())

            self._tree_parser.create_message_tree(self._msg)
            self._tree_parser.parse_message_tree()

            (self._msg_command, self._msg_arguments) = self._tree_parser.get_commands()

            if self._msg_command == "":
                self._msg_tags = self._tree_parser.get_tags()
                self._msg_rating = self._tree_parser.get_rating()

                print(self._command_handler.execute(self._msg_command, [self._msg_tags, self._msg_rating]))

            else:
                print(self._command_handler.execute(self._msg_command, self._msg_arguments))


if __name__ == "__main__":
    patch()

    kernel = Kernel()

    kernel.talk()
