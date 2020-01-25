# -*- coding: utf-8 -*-

from anytree import Node

from core.exceptions import TagNotFoundException, RatingNotFoundException, CommandNotFoundException
from core.logger import class_construct, info, debug, warning, log_func, DEBUG_LOG
from core.utils.json_handler import json_handler
from .string_processor import is_words_similar, prepare_msg


class TreeProcessor(object):
    _tree = None
    _message = None

    _tags = None
    _rating = None
    _command = None
    _argument = None

    _TAG = "TreeProcessor"

    @class_construct
    def __init__(self):
        self._tree = None

        self._command = ""
        self._argument = []

    @log_func(log_write=DEBUG_LOG)
    def _is_command_part(self, string):
        """
        Check string is command part

        :param string: string for check
        :return: True if string is command part, False in other case
        :rtype: bool
        """

        debug(self._TAG, "Check if string '" + string + "' is a command part")

        for j in json_handler.commands_parts:
            if is_words_similar(string, j):
                info(self._TAG, "String '" + string + "' is a command part")
                return True

        return False

    @log_func(log_write=DEBUG_LOG)
    def _is_tag_part(self, string):
        """
        Check string is tag part

        :param string: string for check
        :return: True if string is tag part, False in other case
        :rtype: bool
        """

        debug(self._TAG, "Check if string '" + string + "' is a tag part")

        for j in json_handler.tags_parts:
            if is_words_similar(string, j):
                info(self._TAG, "String '" + string + "' is a tag part")
                return True

        return False

    @log_func(log_write=DEBUG_LOG)
    def _is_ignore(self, string):
        """
        Check string is ignored word

        :param string: string for check
        :return: True if string is ignore, False in other case
        :rtype: bool
        """

        debug(self._TAG, "Check if string '" + string + "' is an ignored word")

        for j in json_handler.ignored:
            if is_words_similar(string, j):
                info(self._TAG, "String '" + string + "' is an ignored word")
                return True

        return False

    @log_func(log_write=DEBUG_LOG)
    def _get_command(self, string):
        """
        Get correct command name

        :param string: command-like string
        :return: correct command or empty string
        :rtype: str
        """

        correct_command = ""

        debug(self._TAG, "Get correct name for '" + string + "' as a command")

        for j in json_handler.commands:
            if is_words_similar(string, j):
                info(self._TAG, "Correct name for '" + string + "' as command is '" + j + "'")
                correct_command = j
                break

        return correct_command

    @log_func(log_write=DEBUG_LOG)
    def _get_tag(self, string):
        """
        Get correct tag name

        :param string: tag-like string
        :return: correct tag or empty string
        :rtype: str
        """

        correct_tag = ""

        debug(self._TAG, "Get correct name for '" + string + "' as a tag")

        for j in json_handler.tags:
            if is_words_similar(string, j):
                info(self._TAG, "Correct name for '" + string + "' as a tag is '" + j + "'")
                correct_tag = j
                break

        return correct_tag

    @log_func(log_write=DEBUG_LOG)
    def _get_rating(self, string):
        """
        Get correct rating name

        :param string: rating name-like string
        :return: correct rating name or empty string
        :rtype: str
        """

        debug(self._TAG, "Get correct name for '" + string + "' as a rating name")

        correct_rating = ""

        for j in json_handler.ratings:
            if is_words_similar(string, j):
                info(self._TAG, "Correct name for '" + string + "' as a rating name is '" + j + "'")
                correct_rating = j

        return correct_rating

    @log_func()
    def create_message_tree(self, raw_message):
        """
        Create tree for input message

        :param raw_message: message from user
        :return: None
        :rtype: None
        """

        self._tree = Node("Message")

        info(self._TAG, "Get message '" + raw_message + "'")
        self._message = prepare_msg(raw_message)
        debug(self._TAG, "Processed message: " + str(self._message))

        tag_parent = self._tree
        command_parent = self._tree

        for i in range(len(self._message)):
            debug(self._TAG, "Processing '" + self._message[i] + "' message part")

            if not (self._is_ignore(self._message[i])):
                if self._is_tag_part(self._message[i]):
                    if i < len(self._message):
                        tag_parent = Node(self._message[i], parent=tag_parent)
                        command_parent = self._tree
                elif self._is_command_part(self._message[i]):
                    if i < len(self._message):
                        command_parent = Node(self._message[i], parent=command_parent)
                        tag_parent = self._tree
                else:
                    debug(self._TAG, "'" + self._message[i] + "' message part is not part of tag or command")

                    command_parent = self._tree
                    tag_parent = self._tree
                    Node(self._message[i], parent=self._tree)
            else:
                continue

    @log_func()
    def parse_message_tree(self):
        """
        Parse tree and grab rating, tags, command and argument from message

        :return: None
        :rtype: None
        """

        tags = []
        rating = ""
        command = ""

        for i in self._tree.children:
            debug(self._TAG, "Process node '" + i.name + "'")

            if i.children == ():
                arg_part = str(i.name)

                debug(self._TAG, "Node '" + i.name + "' has no child. Get correct name as tag")
                name = self._get_tag(str(i.name))  # Process as tag and get correct name if it exist

                # If tag correct name doesn't exist
                if name == "":
                    debug(self._TAG, "Node '" + i.name + "' has no child. Get correct name as command")
                    name = self._get_command(str(i.name))  # Process as command and get correct name if it exist

                    # If command correct name doesn't exist
                    if name == "":
                        debug(self._TAG, "Node '" + i.name + "' has no child. Get correct name as rating")
                        name = self._get_rating(str(i.name))  # Process as rating and get correct name if it exist

                        if name == "":
                            warning(self._TAG, "Node '" + i.name + "' is not a tag, rating or command")
                        else:
                            debug(self._TAG, "Set rating: '" + name + "'")
                            rating = name

                    else:
                        debug(self._TAG, "Set command: '" + name + "'")
                        command = name  # Add command to return
                        arg_part = ""

                else:
                    debug(self._TAG, "Add tag: '" + name + "'")
                    tags.append(name)  # Add tag to return

            else:
                debug(self._TAG, "Node '" + i.name + "' has child. Get it")

                # Get full string from parent and children
                child_name = i.name + " "
                node = i
                while node.children != ():
                    child_name += node.children[0].name + " "
                    node = node.children[0]
                child_name = child_name[:len(child_name) - 1]
                arg_part = child_name

                debug(self._TAG, "Nodes '" + child_name + "' has no child. Get correct name as tag")
                name = self._get_tag(child_name)  # Process as tag and get correct name if it exist

                # If tag correct name doesn't exist
                if name == "":
                    debug(self._TAG, "Nodes '" + child_name + "' has no child. Get correct name as command")
                    name = self._get_command(child_name)  # Process as command and get correct name if it exist

                    if name == "":
                        warning(self._TAG, "Nodes '" + child_name + "' is not a tag, rating or command")
                    else:
                        debug(self._TAG, "Set command: '" + name + "'")
                        command = name  # Add command to return
                        arg_part = ""

                else:
                    debug(self._TAG, "Add tag: '" + name + "'")
                    tags.append(name)  # Add tag to return

            if arg_part != "":
                self._argument.append(arg_part)

        self._tags = tags
        self._command = command
        self._rating = rating

    @log_func()
    def get_tags(self):
        """
        Get tags what contain in user message

        :return: list of tags
        :rtype: list
        """

        try:
            tags = self._tags
            self._tags = None
            return [json_handler.tag_present(x) for x in tags]
        except TagNotFoundException:
            return [""]

    @log_func()
    def get_rating(self):
        """
        Get rating what contains in user message

        :return: rating
        :rtype: str
        """

        try:
            rating = self._rating
            self._rating = None
            return json_handler.rating_present(rating)
        except RatingNotFoundException:
            return ""

    @log_func()
    def get_commands(self):
        """
        Get command what contain in user message

        :return: command and it argument
        :rtype: str, str
        """

        try:
            command = self._command
            argument = self._argument
            self._command = None
            self._argument = []
            return json_handler.command_present(command), argument
        except CommandNotFoundException:
            return "", ""

    @log_func()
    def get_message(self):
        """
        Get split user message

        :return: split user message
        :rtype: list
        """

        return self._message

    @log_func()
    def get_tree(self):
        """
        Get message tree

        :return: message tree
        :rtype: Node
        """

        return self._tree
