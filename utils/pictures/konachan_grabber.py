# -*- coding: utf-8 -*-

import requests

from utils.logger import class_construct, log_func, debug, info, DEBUG_LOG


class KonachanGrabber(object):
    """
    Grabber picture for http://konachan.com/
    """

    _url = None

    @class_construct
    def __init__(self):
        self._url = "http://konachan.com/post.json?tags=%s+rating:%s+order:random&limit=1"

    @log_func(log_write=DEBUG_LOG)
    def get_picture(self, tags, rating):
        """
        Get picture from Konachan

        :param tags: tags of picture
        :param rating: picture rating
        :return: picture url and hash or empty strings
        :rtype: (str, str)
        """

        url = self._url % (tags, rating)

        debug("Get url: " + str(url))

        try:
            picture_object = requests.get(url).json()
        except ConnectionError:
            info("Return empty strings: connection error")
            return "", ""

        debug("Get picture: " + str(picture_object))

        try:
            info("Try to return picture link and hash")
            return picture_object[0]['file_url'], picture_object[0]['md5']

        except:
            info("Return empty strings: picture not found")
            return "", ""
