# -*- coding: utf-8 -*-

import pkg_resources
import json

from utils.logger import class_construct, log_func, debug
from exceptions import TagNotFoundException, RatingNotFoundException, CommandNotFoundException


class StuffHandler(object):
    r"""
    Handler for simple get stuff like a pictures tags, ratings and ignored words
    """

    __resource_package = None
    __resource_path = None

    __all_stuff = None

    @class_construct
    def __init__(self):
        self.__resource_package = __name__
        self.__resource_path = '/'.join(('../static', 'stuff.json'))

        debug("Get reader for " + self.__resource_package + "/" + self.__resource_path)
        template = pkg_resources.resource_stream(self.__resource_package, self.__resource_path)
        line = template.read().decode('utf-8')
        debug("Read data: " + line + ". Proceed in json")
        self.__all_stuff = json.loads(line)
        template.close()

    @property
    @log_func(is_debug=True)
    def commands(self):
        r"""
        Get all commands

        :return: all commands
        :rtype: list
        """

        return list(self.__all_stuff['commands'].keys())

    @property
    @log_func(is_debug=True)
    def commands_parts(self):
        r"""
        Get all possible commands parts

        :return: commands parts
        :rtype: list
        """

        parts = []
        for command_parts in self.__all_stuff['commands'].keys():
            debug("Processing command: " + command_parts)
            if len(command_parts.split(' ')) > 1:
                for part in command_parts.split(' '):
                    debug("Command parts:" + part)
                    if len(part) > 2:
                        parts.append(part)

        return parts

    @log_func(is_debug=True)
    def command_present(self, tag):
        r"""
        Get internal command

        :param tag: user command
        :return: internal command
        :rtype: str
        :raise: CommandNotFoundException if command not found
        """

        try:
            return self.__all_stuff['commands'][tag]
        except KeyError:
            raise CommandNotFoundException
            pass

    @property
    @log_func(is_debug=True)
    def tags(self):
        r"""
        Get all tags

        :return: all tags
        :rtype: list
        """

        return list(self.__all_stuff['tags'].keys())

    @property
    @log_func(is_debug=True)
    def tags_parts(self):
        r"""
        Get all possible tags parts

        :return: tags parts
        :rtype: list
        """

        parts = []
        for i in self.__all_stuff['tags'].keys():
            if len(i.split(' ')) > 1:
                parts += i.split(' ')

        return parts

    @log_func(is_debug=True)
    def tag_present(self, tag):
        r"""
        Get tag present on Konachan and Yandere

        :param tag: tag for present
        :return: tag present
        :rtype: str
        :raise: TagNotFoundException if tag not found
        """

        try:
            return self.__all_stuff['tags'][tag]
        except KeyError:
            raise TagNotFoundException
            pass

    @property
    @log_func(is_debug=True)
    def ratings(self):
        r"""
        Get all ratings

        :return: all ratings
        :rtype: list
        """

        return list(self.__all_stuff['ratings'].keys())

    @log_func(is_debug=True)
    def rating_present(self, rating):
        r"""
        Get rating present on Konachan and Yandere

        :param rating: rating for present
        :return: rating present
        :rtype: str
        :raise: RatingNotFoundException if rating not found
        """

        try:
            return self.__all_stuff['ratings'][rating]
        except KeyError:
            raise RatingNotFoundException
            pass

    @property
    @log_func(is_debug=True)
    def ignored_words(self):
        r"""
        Get all ignored words

        :return: all ignored words
        :rtype: list
        """

        return self.__all_stuff['ignored']
