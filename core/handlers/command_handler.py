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
    def __init__(self, command, arguments):
        """
        Constructor for CommandProcessor

        :param command: command from user
        :param arguments: command argument
        """
        self._command = command
        self._argument = arguments

        self._handler = JsonHandler()

        self._actions = {
            "about": self._about,
            "hello": self._hello,
            "": self._picture,
            "roll": self._roll
        }

    def execute(self):
        """
        Call function for command

        :return: None
        :rtype: None
        """
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
        """
        grabber = PictureGrabber()

        try:
            grabber.get_picture(self._argument[1], self._argument[0])

            return self._handler.messages['picture_answer']
        except PictureNotFoundException:
            return self._handler.messages['no_picture_answer']

    def _roll(self):
        """
        Choice of two options

        :return: one of two
        """

        num = random.randint(1, 100)

        return self._argument[0] if num < 50 else self._argument[1]
