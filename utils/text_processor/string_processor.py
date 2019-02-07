# -*- coding: utf-8 -*-

import logging

from anytree import Node

from utils.stuff_handler import StuffHandler
from .utils import distance, prepare_msg
from utils.logger import class_construct, info, debug, log_func


class StringProcessor(object):

    __handler = None
    __tree = None
    __message = None

    __tag_part_distance = None
    __tag_simple_distance = None
    __tag_distance = None

    __com_part_distance = None
    __com_simple_distance = None
    __com_distance = None

    __rating_name_distance = None
    __rating_distance = None

    @class_construct
    def __init__(self):
        self.__handler = StuffHandler()
        self.__tree = Node("Message")

        self.__com_part_distance = 3
        self.__com_simple_distance = 3
        self.__com_distance = 8

        self.__tag_part_distance = 4
        self.__tag_simple_distance = 3
        self.__tag_distance = 8

        self.__rating_name_distance = 3
        self.__rating_distance = 4

    @log_func(is_debug=True)
    def __is_command_part(self, string):
        r"""
        Check string is command part

        :param string: string for check
        :return: True if string is command part, False in other case
        :rtype: bool
        """

        commands_parts = self.__handler.commands_parts
        min_distance = distance(string, commands_parts[0])

        debug("Processing string '" + string + "'  as command part")

        for j in commands_parts:
            current_distance = distance(string, j)

            debug("Current distance between " + string + " and " + j + " is " + str(current_distance))

            if current_distance < min_distance:
                min_distance = current_distance

        if min_distance < self.__com_part_distance:
            return True
        return False

    @log_func(is_debug=True)
    def __get_simple_command(self, string):
        r"""
        Get correct one-word command

        :param string: command-like string
        :return: correct command or empty string
        :rtype: str
        """

        debug("Processing string '" + string + "' as simple command")

        if not self.__is_tag_part(string) and not self.__is_rating_name(string) and not self.__is_command_part(string):
            commands = self.__handler.commands
            correct_command = commands[0]
            min_distance = distance(string, correct_command)

            debug("String '" + string + "' is simple command")

            for j in commands:
                current_distance = distance(string, j)

                debug("Current distance between " + string + " and " + j + " is " + str(current_distance))

                if current_distance < min_distance:
                    min_distance = current_distance
                    correct_command = j

            if min_distance < self.__com_simple_distance:
                return correct_command
            return ""

        return ""

    @log_func(is_debug=True)
    def __get_command(self, string):
        r"""
        Get correct complex command

        :param string: command-like string
        :return: correct command or empty string
        :rtype: str
        """

        commands = self.__handler.commands
        correct_command = commands[0]
        min_distance = distance(string, correct_command)

        debug("Processing string '" + string + "' as command")

        for j in commands:
            current_distance = distance(string, j)

            debug("Current distance between " + string + " and " + j + " is " + str(current_distance))

            if current_distance < min_distance:
                min_distance = current_distance
                correct_command = j

        if min_distance < self.__com_distance:
            return correct_command
        return ""

    @log_func(is_debug=True)
    def __is_tag_part(self, string):
        r"""
        Check string is tag part

        :param string: string for check
        :return: True if string is tag part, False in other case
        :rtype: bool
        """

        tags_parts = self.__handler.tags_parts
        min_distance = distance(string, tags_parts[0])

        debug("Processing string '" + string + "' as tag part")

        for j in tags_parts:
            current_distance = distance(string, j)

            debug("Current distance between " + string + " and " + j + " is " + str(current_distance))

            if current_distance < min_distance:
                min_distance = current_distance

        if min_distance < self.__tag_part_distance:
            return True
        return False

    @log_func(is_debug=True)
    def __get_simple_tag(self, string):
        r"""
        Get correct one-word tag

        :param string: tag-like string
        :return: correct tag or empty string
        :rtype: str
        """

        debug("Processing string '" + string + "' as simple tag")

        if not self.__is_tag_part(string) and not self.__is_rating_name(string) and not self.__is_command_part(string):
            tags = self.__handler.tags
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

    @log_func(is_debug=True)
    def __get_tag(self, string):
        r"""
        Get correct complex tag

        :param string: tag-like string
        :return: correct tag or empty string
        :rtype: str
        """

        tags = self.__handler.tags
        correct_tag = tags[0]
        min_distance = distance(string, correct_tag)

        debug("Processing string '" + string + "' as tag")

        for j in tags:
            current_distance = distance(string, j)

            debug("Current distance between " + string + " and " + j + " is " + str(current_distance))

            if current_distance < min_distance:
                min_distance = current_distance
                correct_tag = j

        if min_distance < self.__tag_distance:
            return correct_tag
        return ""

    @log_func(is_debug=True)
    def __is_rating_name(self, string):
        r"""
        Check string is rating name

        :param string: rating-like string
        :return: True if string is rating, False in other case
        :rtype: bool
        """

        ratings = self.__handler.ratings
        min_distance = distance(string, ratings[0])

        debug("Processing string '" + string + "' for check rating name")

        for j in ratings:
            current_distance = distance(string, j)

            debug("Current distance between " + string + " and " + j + " is " + str(current_distance))

            if current_distance < min_distance:
                min_distance = current_distance

        if min_distance < self.__rating_name_distance:
            return True
        return False

    @log_func(is_debug=True)
    def __get_rating(self, string):
        r"""
        Get correct rating

        :param string: rating-like string
        :return: correct rating or empty string
        :rtype: bool
        """

        debug("Processing string '" + string + "' as rating")

        if self.__is_rating_name(string):
            ratings = self.__handler.ratings
            correct_name = ratings[0]
            min_distance = distance(string, correct_name)

            debug("String '" + string + "' is rating")

            for j in ratings:
                current_distance = distance(string, j)

                debug("Current distance between " + string + " and " + j + " is " + str(current_distance))

                if current_distance < min_distance:
                    min_distance = current_distance
                    correct_name = j

            if min_distance < self.__rating_distance:
                return correct_name
            return ""

        return ""

    @log_func()
    def create_message_tree(self, raw_message):
        r"""
        Create tree for input message

        :param raw_message: message from user
        :return: None
        :rtype: None
        """

        info("Get message " + raw_message)
        self.__message = prepare_msg(raw_message)
        debug("Processed message: " + str(self.__message))

        tag_parent = self.__tree
        command_parent = self.__tree

        for i in range(len(self.__message)):
            debug("Processing '" + self.__message[i] + "' message part")

            if self.__message[i] not in self.__handler.ignored_words:
                debug(self.__message[i] + " message part is not ignored word")

                if self.__is_tag_part(self.__message[i]):
                    debug(self.__message[i] + " message part is tag part")

                    if i < len(self.__message):
                        tag_parent = Node(self.__message[i], parent=tag_parent)
                        command_parent = self.__tree
                elif self.__is_command_part(self.__message[i]):
                    debug(self.__message[i] + " message part is command part")

                    if i < len(self.__message):
                        command_parent = Node(self.__message[i], parent=command_parent)
                        tag_parent = self.__tree
                else:
                    debug(self.__message[i] + " message part is smth else")

                    command_parent = self.__tree
                    tag_parent = self.__tree
                    Node(self.__message[i], parent=self.__tree)

    @log_func()
    def get_tags(self):
        r"""
        Get tags what contain in user message

        :return: list of tags
        :rtype: list
        """

        tags = []

        for i in self.__tree.children:
            debug("Process node " + str(i.name))

            if i.children == ():

                debug("Node " + str(i.name) + " has no child. Get correct name")
                name = self.__get_simple_tag(i.name)
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
                name = self.__get_tag(child_name)
                debug("Correct name: " + str(name))

                if name != "":
                    tags.append(name)

        info("Found tags: " + str(tags))
        return tags

    @log_func()
    def get_rating(self):
        r"""
        Get rating what contains in user message

        :return: rating
        :rtype: str
        """

        rating = ""

        for i in self.__tree.children:
            debug("Process node " + str(i.name))
            if self.__is_rating_name(i.name):
                logging.debug("Found rating " + str(i.name))
                rating = self.__get_rating(i.name)
                break

        info("Found rating " + rating)

        return rating

    @log_func()
    def get_commands(self):
        r"""
        Get commands what contain in user message

        :return: list of commands
        :rtype: list
        """

        commands = []

        for i in self.__tree.children:
            debug("Process node " + str(i.name))

            if i.children == ():

                debug("Node " + str(i.name) + " has no child. Get correct name")
                name = self.__get_simple_command(i.name)
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
                name = self.__get_command(child_name)
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

        return self.__message

    @log_func()
    def get_tree(self):
        r"""
        Get message tree

        :return: message tree
        :rtype: Node
        """

        return self.__tree
