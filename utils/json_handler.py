# -*- coding: utf-8 -*-

import json

import pkg_resources

from core import TagNotFoundException, RatingNotFoundException, CommandNotFoundException
from utils.logger import class_construct, log_func, debug, DEBUG_LOG


class JsonHandler(object):
    """
    Handler for simple get stuff like a pictures tags, ratings and ignored words
    """

    _resource_package = None
    _resource_path = None

    _tags = None
    _commands = None
    _ratings = None
    _ignored = None
    _ignored_words = None

    _consts = None
    _messages = None

    @class_construct
    def __init__(self):
        self._resource_package = __name__

        self._resource_path = '/'.join(('../static', 'tags.json'))
        debug("Get reader for " + self._resource_package + "/" + self._resource_path)
        template = pkg_resources.resource_stream(self._resource_package, self._resource_path)
        line = template.read().decode('utf-8')
        debug("Read data: " + line + ". Proceed in json")
        self._tags = json.loads(line)['tags']
        template.close()

        self._resource_path = '/'.join(('../static', 'commands.json'))
        debug("Get reader for " + self._resource_package + "/" + self._resource_path)
        template = pkg_resources.resource_stream(self._resource_package, self._resource_path)
        line = template.read().decode('utf-8')
        debug("Read data: " + line + ". Proceed in json")
        self._commands = json.loads(line)['commands']
        template.close()

        self._resource_path = '/'.join(('../static', 'ratings.json'))
        debug("Get reader for " + self._resource_package + "/" + self._resource_path)
        template = pkg_resources.resource_stream(self._resource_package, self._resource_path)
        line = template.read().decode('utf-8')
        debug("Read data: " + line + ". Proceed in json")
        self._ratings = json.loads(line)['ratings']
        template.close()

        self._resource_path = '/'.join(('../static', 'ignored.json'))
        debug("Get reader for " + self._resource_package + "/" + self._resource_path)
        template = pkg_resources.resource_stream(self._resource_package, self._resource_path)
        line = template.read().decode('utf-8')
        debug("Read data: " + line + ". Proceed in json")
        self._ignored = json.loads(line)['ignored']
        self._ignored_words = json.loads(line)['words']
        template.close()

        self._resource_path = '/'.join(('../static', 'consts.json'))
        debug("Get reader for " + self._resource_package + "/" + self._resource_path)
        template = pkg_resources.resource_stream(self._resource_package, self._resource_path)
        line = template.read().decode('utf-8')
        debug("Read data: " + line + ". Proceed in json")
        self._consts = json.loads(line)
        template.close()

        self._resource_path = '/'.join(('../static', 'messages.json'))
        debug("Get reader for " + self._resource_package + "/" + self._resource_path)
        template = pkg_resources.resource_stream(self._resource_package, self._resource_path)
        line = template.read().decode('utf-8')
        debug("Read data: " + line + ". Proceed in json")
        self._messages = json.loads(line)
        template.close()

    @property
    @log_func(log_write=DEBUG_LOG)
    def commands(self):
        """
        Get all commands

        :return: all commands
        :rtype: list
        """

        return list(self._commands.keys())

    @property
    @log_func(log_write=DEBUG_LOG)
    def commands_parts(self):
        """
        Get all possible commands parts

        :return: commands parts
        :rtype: list
        """

        parts = []
        for command_parts in self._commands.keys():
            debug("Processing command: " + command_parts)
            if len(command_parts.split(' ')) > 1:
                for part in command_parts.split(' '):
                    debug("Command parts:" + part)
                    if len(part) > 2:
                        parts.append(part)

        return parts

    @log_func(log_write=DEBUG_LOG)
    def command_present(self, command):
        """
        Get internal command

        :param command: user command
        :return: internal command
        :rtype: str
        :raise: CommandNotFoundException if command not found
        """

        try:
            return self._commands[command]
        except KeyError:
            raise CommandNotFoundException()
            pass

    @property
    @log_func(log_write=DEBUG_LOG)
    def tags(self):
        """
        Get all tags

        :return: all tags
        :rtype: list
        """

        return list(self._tags.keys())

    @property
    @log_func(log_write=DEBUG_LOG)
    def tags_parts(self):
        """
        Get all possible tags parts

        :return: tags parts
        :rtype: list
        """

        parts = []
        for i in self._tags.keys():
            if len(i.split(' ')) > 1:
                parts += i.split(' ')

        return parts

    @log_func(log_write=DEBUG_LOG)
    def tag_present(self, tag):
        """
        Get tag present on Konachan and Yandere

        :param tag: tag for present
        :return: tag present
        :rtype: str
        :raise: TagNotFoundException if tag not found
        """

        try:
            return self._tags[tag]
        except KeyError:
            raise TagNotFoundException()
            pass

    @property
    @log_func(log_write=DEBUG_LOG)
    def ratings(self):
        """
        Get all ratings

        :return: all ratings
        :rtype: list
        """

        return list(self._ratings.keys())

    @log_func(log_write=DEBUG_LOG)
    def rating_present(self, rating):
        """
        Get rating present on Konachan and Yandere

        :param rating: rating for present
        :return: rating present
        :rtype: str
        :raise: RatingNotFoundException if rating not found
        """

        try:
            return self._ratings[rating]
        except KeyError:
            raise RatingNotFoundException()
            pass

    @property
    @log_func(log_write=DEBUG_LOG)
    def ignored(self):
        """
        Get all ignored words

        :return: all ignored words
        :rtype: list
        """

        return self._ignored

    @property
    @log_func(log_write=DEBUG_LOG)
    def ignored_words(self):
        """
        Get all ignored words

        :return: all ignored words
        :rtype: list
        """

        return self._ignored_words

    @property
    @log_func(log_write=DEBUG_LOG)
    def constants(self):
        """
        Get app constants

        :return: app constants
        :rtype: dict
        """

        return self._consts

    @property
    @log_func(log_write=DEBUG_LOG)
    def messages(self):
        """
        Get messages for send as answer

        :return: messages templates
        :rtype: dict
        """

        return self._messages
