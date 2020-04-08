# -*- coding: utf-8 -*-

#   Copyright (c) 2020.
#  #
#   Created by AnyKeyShik Rarity
#  #
#   Telegram: @AnyKeyShik
#   GitHub: https://github.com/AnyKeyShik
#   E-mail: nikitag594@gmail.com

import json

import pkg_resources

from core.exceptions import TagNotFoundException, RatingNotFoundException, CommandNotFoundException
from . import logger


class JsonHandler(object):
    """
    Handler for simple get stuff like a pictures tags, ratings and ignored words
    """
    def __init__(self):
        self._resource_package = __name__

        self._resource_path = '/'.join(('../../static', 'tags.json'))
        template = pkg_resources.resource_stream(self._resource_package, self._resource_path)
        line = template.read().decode('utf-8')
        self._tags = json.loads(line)['tags']
        self._tags_user = json.loads(line)['user_tags']
        logger.debug("Get tags list for user")
        template.close()

        self._resource_path = '/'.join(('../../static', 'commands.json'))
        template = pkg_resources.resource_stream(self._resource_package, self._resource_path)
        line = template.read().decode('utf-8')
        self._commands = json.loads(line)['commands']
        self._commands_user = json.loads(line)['commands_user']
        logger.debug("Get command list for user")
        template.close()

        self._resource_path = '/'.join(('../../static', 'ratings.json'))
        template = pkg_resources.resource_stream(self._resource_package, self._resource_path)
        line = template.read().decode('utf-8')
        self._ratings = json.loads(line)['ratings']
        logger.debug("Get ratings")

        template.close()

        self._resource_path = '/'.join(('../../static', 'ignored.json'))
        template = pkg_resources.resource_stream(self._resource_package, self._resource_path)
        line = template.read().decode('utf-8')
        self._ignored = json.loads(line)['words']
        logger.debug("Get list of ignored words")
        template.close()

        self._resource_path = '/'.join(('../../static', 'consts.json'))
        template = pkg_resources.resource_stream(self._resource_package, self._resource_path)
        line = template.read().decode('utf-8')
        self._consts = json.loads(line)
        logger.debug("Get constants")
        template.close()

        self._resource_path = '/'.join(('../../static', 'auth_consts.json'))
        template = pkg_resources.resource_stream(self._resource_package, self._resource_path)
        line = template.read().decode('utf-8')
        self._auth_consts = json.loads(line)
        logger.debug("Get authentication data")
        template.close()

        self._resource_path = '/'.join(('../../static', 'messages.json'))
        template = pkg_resources.resource_stream(self._resource_package, self._resource_path)
        line = template.read().decode('utf-8')
        self._messages = json.loads(line)
        logger.debug("Get messages for answers")
        template.close()

    @property
    def commands(self):
        """
        Get all commands

        :return: all commands
        :rtype: list
        """

        return list(self._commands.keys())

    @property
    def commands_user(self):
        """
        Get all commands with description

        :return: all commands with description
        :rtype: str
        """

        return "\n".join([x + ' - ' + self._commands_user[x] for x in self._commands_user])

    @property
    def commands_parts(self):
        """
        Get all possible commands parts

        :return: commands parts
        :rtype: list
        """

        parts = []
        for command_parts in self._commands.keys():
            if len(command_parts.split(' ')) > 1:
                for part in command_parts.split(' '):
                    if len(part) > 2:
                        parts.append(part)

        return parts

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

    @property
    def tags(self):
        """
        Get all tags

        :return: all tags
        :rtype: list
        """

        return list(self._tags.keys())

    @property
    def tags_user(self):
        """
        Get all tags for user

        :return: all tags for user
        :rtype: str
        """

        return "\n".join(self._tags_user)

    @property
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

    @property
    def ratings(self):
        """
        Get all ratings

        :return: all ratings
        :rtype: list
        """

        return list(self._ratings.keys())

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

    @property
    def ignored(self):
        """
        Get all ignored words

        :return: all ignored words
        :rtype: list
        """

        return self._ignored

    @property
    def constants(self):
        """
        Get app constants

        :return: app constants
        :rtype: dict
        """

        return self._consts

    @property
    def auth_constants(self):
        """
        Get app constants for auth

        :return: app constants for auth
        :rtype: dict
        """

        return self._auth_consts

    @property
    def messages(self):
        """
        Get messages for send as answer

        :return: messages templates
        :rtype: dict
        """

        return self._messages


json_handler = JsonHandler()
