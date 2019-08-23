# -*- coding: utf-8 -*-

import random

from core.exceptions import AnimeNotFoundException, PictureNotFoundException
from utils import ShikimoriGrabber, PictureGrabber
from utils.json_handler import JsonHandler
from utils.logger import class_construct


class CommandProcessor(object):
    _command = None
    _argument = None

    _actions = None
    _handler = None

    @class_construct
    def __init__(self):
        """
        Constructor for CommandProcessor
        """

        self._handler = JsonHandler()

        self._actions = {
            "about": self._about,
            "hello": self._hello,
            "": self._picture,
            "roll": self._roll,
            "tags": self._tags,
            "commands": self._commands,
            "error": self._error
        }

    def execute(self, command, arguments):
        """
        Call function for command

        :param command: command from user
        :param arguments: command argument
        :return: None
        :rtype: None
        """

        self._command = command
        self._argument = arguments

        return self._actions[self._command]()

    def _about(self):
        """
        Comment about anime form Shikimori

        :return: comment for anime
        :rtype: str
        """
        grabber = ShikimoriGrabber()

        try:
            return grabber.get_anime(self._argument[0])
        except AnimeNotFoundException:
            return self._handler.messages['no_anime_answer'] + self._argument[0]

    def _hello(self):
        """
        Hello message

        :return: hello message
        :rtype: str
        """
        return self._handler.messages['hello_answer']

    def _picture(self):
        """
        Picture by tag and rating

        :return: picture url
        :rtype: str
        """
        grabber = PictureGrabber()

        try:
            grabber.get_picture(self._argument[0], self._argument[1])

            return self._handler.messages['picture_answer']
        except PictureNotFoundException:
            return self._handler.messages['no_picture_answer']

    def _roll(self):
        """
        Choice of provided options

        :return: one of many
        :rtype: str
        """

        sentence = " ".join(self._argument)
        choices = sentence.split(" или ")

        if len(choices) > 1:

            num = random.randint(1, 100 * len(choices))

            return choices[num // 100]
        else:
            return self._handler.messages['no_choices']

    def _tags(self):
        """
        List of avialivle tags

        :return: list of tags
        :rtype: str
        """

        return self._handler.tags_user

    def _commands(self):
        """
        List of avialivle commands

        :return: list of commands
        :rtype: str
        """

        return self._handler.commands_user

    def _error(self):
        """
        Message with bugs description

        :return: bug message
        :rtype: str
        """
        return self._handler.messages['errors_answer']
