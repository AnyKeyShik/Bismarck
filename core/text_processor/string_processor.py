# -*- coding: utf-8 -*-

import logging

from anytree import Node

from utils.json_handler import StuffHandler
from utils.logger import class_construct, info, debug, log_func, DEBUG_LOG
from .utils import distance, prepare_msg


class StringProcessor(object):
    _handler = None
    _tree = None
    _message = None

    _tag_part_distance = None
    _tag_simple_distance = None
    _tag_distance = None

    _com_part_distance = None
    _com_simple_distance = None
    _com_distance = None

    _rating_name_distance = None
    _rating_distance = None

    @class_construct
    def __init__(self):
        self._handler = StuffHandler()
        self._tree = Node("Message")

        self._com_part_distance = 3
        self._com_simple_distance = 3
        self._com_distance = 8

        self._tag_part_distance = 4
        self._tag_simple_distance = 3
        self._tag_distance = 8

        self._rating_name_distance = 3
        self._rating_distance = 4

    @log_func(log_write=DEBUG_LOG)
    def _is_command_part(self, string):
        """
        Check string is command part

        :param string: string for check
        :return: True if string is command part, False in other case
        :rtype: bool
        """

        commands_parts = self._handler.commands_parts
        min_distance = distance(string, commands_parts[0])

        debug("Processing string '" + string + "'  as command part")

        for j in commands_parts:
            current_distance = distance(string, j)

            debug("Current distance between " + string + " and " + j + " is " + str(current_distance))

            if current_distance < min_distance:
                min_distance = current_distance

        if min_distance < self._com_part_distance:
            return True
        return False

    @log_func(log_write=DEBUG_LOG)
    def _get_simple_command(self, string):
        """
        Get correct one-word command

        :param string: command-like string
        :return: correct command or empty string
        :rtype: str
        """

        debug("Processing string '" + string + "' as simple command")

        if not self._is_tag_part(string) and not self._is_rating_name(string) and not self._is_command_part(string):
            commands = self._handler.commands
            correct_command = commands[0]
            min_distance = distance(string, correct_command)

            debug("String '" + string + "' is simple command")

            for j in commands:
                current_distance = distance(string, j)

                debug("Current distance between " + string + " and " + j + " is " + str(current_distance))

                if current_distance < min_distance:
                    min_distance = current_distance
                    correct_command = j

            if min_distance < self._com_simple_distance:
                return correct_command
            return ""

        return ""

    @log_func(log_write=DEBUG_LOG)
    def _get_command(self, string):
        """
        Get correct complex command

        :param string: command-like string
        :return: correct command or empty string
        :rtype: str
        """

        commands = self._handler.commands
        correct_command = commands[0]
        min_distance = distance(string, correct_command)

        debug("Processing string '" + string + "' as command")

        for j in commands:
            current_distance = distance(string, j)

            debug("Current distance between " + string + " and " + j + " is " + str(current_distance))

            if current_distance < min_distance:
                min_distance = current_distance
                correct_command = j

        if min_distance < self._com_distance:
            return correct_command
        return ""

    @log_func(log_write=DEBUG_LOG)
    def _is_tag_part(self, string):
        """
        Check string is tag part

        :param string: string for check
        :return: True if string is tag part, False in other case
        :rtype: bool
        """

        tags_parts = self._handler.tags_parts
        min_distance = distance(string, tags_parts[0])

        debug("Processing string '" + string + "' as tag part")

        for j in tags_parts:
            current_distance = distance(string, j)

            debug("Current distance between " + string + " and " + j + " is " + str(current_distance))

            if current_distance < min_distance:
                min_distance = current_distance

        if min_distance < self._tag_part_distance:
            return True
        return False

    @log_func(log_write=DEBUG_LOG)
    def _get_simple_tag(self, string):
        """
        Get correct one-word tag

        :param string: tag-like string
        :return: correct tag or empty string
        :rtype: str
        """

        debug("Processing string '" + string + "' as simple tag")

        if not self._is_tag_part(string) and not self._is_rating_name(string) and not self._is_command_part(string):
            tags = self._handler.tags
            correct_tag = tags[0]
            min_distance = distance(string, correct_tag)

            debug("String '" + string + "' is simple tag")

            for j in tags:
                current_distance = distance(string, j)

                debug("Current distance between " + string + " and " + j + " is " + str(current_distance))

                if current_distance < min_distance:
                    min_distance = current_distance
                    correct_tag = j

            if min_distance < 3:
                return correct_tag
            return ""

        return ""

    @log_func(log_write=DEBUG_LOG)
    def _get_tag(self, string):
        """
        Get correct complex tag

        :param string: tag-like string
        :return: correct tag or empty string
        :rtype: str
        """

        tags = self._handler.tags
        correct_tag = tags[0]
        min_distance = distance(string, correct_tag)

        debug("Processing string '" + string + "' as tag")

        for j in tags:
            current_distance = distance(string, j)

            debug("Current distance between " + string + " and " + j + " is " + str(current_distance))

            if current_distance < min_distance:
                min_distance = current_distance
                correct_tag = j

        if min_distance < self._tag_distance:
            return correct_tag
        return ""

    @log_func(log_write=DEBUG_LOG)
    def _is_rating_name(self, string):
        """
        Check string is rating name

        :param string: rating-like string
        :return: True if string is rating, False in other case
        :rtype: bool
        """

        ratings = self._handler.ratings
        min_distance = distance(string, ratings[0])

        debug("Processing string '" + string + "' for check rating name")

        for j in ratings:
            current_distance = distance(string, j)

            debug("Current distance between " + string + " and " + j + " is " + str(current_distance))

            if current_distance < min_distance:
                min_distance = current_distance

        if min_distance < self._rating_name_distance:
            return True
        return False

    @log_func(log_write=DEBUG_LOG)
    def _get_rating(self, string):
        """
        Get correct rating

        :param string: rating-like string
        :return: correct rating or empty string
        :rtype: bool
        """

        debug("Processing string '" + string + "' as rating")

        if self._is_rating_name(string):
            ratings = self._handler.ratings
            correct_name = ratings[0]
            min_distance = distance(string, correct_name)

            debug("String '" + string + "' is rating")

            for j in ratings:
                current_distance = distance(string, j)

                debug("Current distance between " + string + " and " + j + " is " + str(current_distance))

                if current_distance < min_distance:
                    min_distance = current_distance
                    correct_name = j

            if min_distance < self._rating_distance:
                return correct_name
            return ""

        return ""

    @log_func()
    def create_message_tree(self, raw_message):
        """
        Create tree for input message

        :param raw_message: message from user
        :return: None
        :rtype: None
        """

        info("Get message " + raw_message)
        self._message = prepare_msg(raw_message)
        debug("Processed message: " + str(self._message))

        tag_parent = self._tree
        command_parent = self._tree

        for i in range(len(self._message)):
            debug("Processing '" + self._message[i] + "' message part")

            if self._message[i] not in self._handler.ignored_words:
                debug(self._message[i] + " message part is not ignored word")

                if self._is_tag_part(self._message[i]):
                    debug(self._message[i] + " message part is tag part")

                    if i < len(self._message):
                        tag_parent = Node(self._message[i], parent=tag_parent)
                        command_parent = self._tree
                elif self._is_command_part(self._message[i]):
                    debug(self._message[i] + " message part is command part")

                    if i < len(self._message):
                        command_parent = Node(self._message[i], parent=command_parent)
                        tag_parent = self._tree
                else:
                    debug(self._message[i] + " message part is smth else")

                    command_parent = self._tree
                    tag_parent = self._tree
                    Node(self._message[i], parent=self._tree)

    @log_func()
    def get_tags(self):
        """
        Get tags what contain in user message

        :return: list of tags
        :rtype: list
        """

        tags = []

        for i in self._tree.children:
            debug("Process node " + str(i.name))

            if i.children == ():

                debug("Node " + str(i.name) + " has no child. Get correct name")
                name = self._get_simple_tag(i.name)
                debug("Correct name: " + str(name))

                if name != "":
                    tags.append(name)

            else:
                debug("Node " + str(i.name) + " has child. Get it")

                child_name = i.name + " "
                node = i

                while node.children != ():
                    child_name += node.children[0].name + " "
                    node = node.children[0]

                child_name = child_name[:len(child_name) - 1]

                debug("Complete name: " + child_name + ". Get correct name")
                name = self._get_tag(child_name)
                debug("Correct name: " + str(name))

                if name != "":
                    tags.append(name)

        info("Found tags: " + str(tags))
        return tags

    @log_func()
    def get_rating(self):
        """
        Get rating what contains in user message

        :return: rating
        :rtype: str
        """

        rating = ""

        for i in self._tree.children:
            debug("Process node " + str(i.name))
            if self._is_rating_name(i.name):
                logging.debug("Found rating " + str(i.name))
                rating = self._get_rating(i.name)
                break

        info("Found rating " + rating)

        return rating

    @log_func()
    def get_commands(self):
        """
        Get commands what contain in user message

        :return: list of commands
        :rtype: list
        """

        commands = []

        for i in self._tree.children:
            debug("Process node " + str(i.name))

            if i.children == ():

                debug("Node " + str(i.name) + " has no child. Get correct name")
                name = self._get_simple_command(i.name)
                debug("Correct name: " + str(name))

                if name != "":
                    commands.append(name)

            else:
                debug("Node " + str(i.name) + " has child. Get it")

                child_name = i.name + " "
                node = i

                while node.children != ():
                    child_name += node.children[0].name + " "
                    node = node.children[0]

                child_name = child_name[:len(child_name) - 1]

                debug("Complete name: " + child_name + ". Get correct name")
                name = self._get_command(child_name)
                debug("Correct name: " + str(name))

                if name != "":
                    commands.append(name)

        info("Found commands: " + str(commands))
        return commands

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
