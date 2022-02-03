# -*- coding: utf-8 -*-

#   Copyright (c) 2020.
#
#   Created by AnyKeyShik Rarity
#
#   Telegram: @AnyKeyShik
#   GitHub: https://github.com/AnyKeyShik
#   E-mail: nikitag594@gmail.com

import random

from core.exceptions import AnimeNotFoundException, PictureNotFoundException, TagsNotFoundException, \
    EcchiDeniedException, HentaiDeniedException
from core.utils import ShikimoriGrabber, PictureGrabber
from core.utils.json_handler import json_handler
from . import logger


class CommandProcessor(object):
    _command = None
    _argument = None

    _TAG = "CommandProcessor"

    _actions = None

    @logger.class_construct
    def __init__(self):
        """
        Constructor for CommandProcessor
        """

        self._actions = {
            "about": self._about,
            "hello": self._hello,
            "": self._picture,
            "roll": self._roll,
            "tags": self._tags,
            "commands": self._commands,
            "error": self._error,
            "kek": self._kek
        }

    def execute(self, command, arguments):
        """
        Call function for command

        :param command: command from user
        :param arguments: command argument
        :return: string with answer for user (in some case returning pair of str)
        :rtype: str or (str, str)
        """

        self._command = command
        self._argument = arguments

        logger.debug("Execute \"" + str(command) + "\" with arguments " + str(arguments))

        return self._actions[self._command]()

    def _about(self):
        """
        Comment about anime form Shikimori

        :return: comment for anime
        :rtype: str
        """
        grabber = ShikimoriGrabber()
        anime_name = ' '.join(self._argument)

        try:
            if len(anime_name) > 0:
                return grabber.get_anime(anime_name)
            else:
                return json_handler.messages['no_anime_given_answer']
        except AnimeNotFoundException:
            return json_handler.messages['no_anime_answer'] + anime_name

    @staticmethod
    def _hello():
        """
        Hello message

        :return: hello message
        :rtype: str
        """
        return json_handler.messages['hello_answer']

    def _picture(self):
        """
        Picture by tag and rating

        :return: pair of picture url and filename
        :rtype: (str, str)
        """
        grabber = PictureGrabber()

        try:
            grabber.get_picture(self._argument[0], self._argument[1], self._argument[2])

            return json_handler.messages['picture_answer'], json_handler.constants['default_picture_file']
        except PictureNotFoundException:
            return json_handler.messages['no_picture_answer'], json_handler.constants['picture_not_found_file']
        except TagsNotFoundException:
            return json_handler.messages['no_tags_answer'], json_handler.constants['no_tags_found_file']
        except EcchiDeniedException:
            return json_handler.messages['ecchi_denied_answer'], json_handler.constants['ecchi_denied_file']
        except HentaiDeniedException:
            return json_handler.messages['hentai_denied_answer'], json_handler.constants['hentai_denied_file']
        except Exception as err:
            logger.error("Download error: {0}".format(err))
            return json_handler.messages['download_error_answer'], json_handler.constants['download_error_file']

    def _roll(self):
        """
        Choice of provided options

        :return: one of many
        :rtype: str
        """

        sentence = " ".join(self._argument)
        choices = sentence.split("или")

        while choices.count("или") != 0:
            choices.remove("или")

        for index, word in enumerate(choices):
            if word.find(" ") == 0:
                choices[index] = word.replace(" ", "", 1)
            if word.rfind(" ") == len(word) - 1:
                choices[index] = word[:len(word) - 1]

        choices = list(filter(None, choices))

        logger.info("Available choices: " + str(choices))

        if len(choices) > 1:

            num = random.randint(1, 100 * len(choices))

            return choices[num // 100]
        else:
            return json_handler.messages['no_choices_answer']

    @staticmethod
    def _kek():
        """
        Just KEK

        :return: KEK
        :rtype: str
        """

        return json_handler.messages['kek']

    @staticmethod
    def _tags():
        """
        List of available tags

        :return: list of tags
        :rtype: str
        """

        return json_handler.tags_user

    @staticmethod
    def _commands():
        """
        List of available commands

        :return: list of commands
        :rtype: str
        """

        return json_handler.commands_user

    @staticmethod
    def _error():
        """
        Message with bugs description

        :return: bug message
        :rtype: str
        """
        return json_handler.messages['errors_answer']
