# -*- coding: utf-8 -*-

from json.decoder import JSONDecodeError

import requests

from core.utils.logger import log_func, debug, info, DEBUG_LOG


class Grabber(object):
    _url = ""

    @log_func(log_write=DEBUG_LOG)
    def get_picture(self, tags, rating):
        """
        Get picture from Konachan

        :param tags: tags of picture
        :param rating: picture rating
        :return: picture url and hash or empty strings
        :rtype: (str, str)
        """
        info("get_picture()")

        url = self._url % (tags, rating)

        debug("Get url: " + str(url))

        try:
            picture_object = requests.get(url).json()
        except ConnectionError:
            info("Return empty strings: connection error")
            return "", ""
        except JSONDecodeError:
            info("Picture not found")
            return "", ""

        debug("Get picture: " + str(picture_object))

        try:
            info("Try to return picture link and hash")
            return picture_object[0]['file_url'], picture_object[0]['md5']

        except:
            info("Return empty strings: picture not found")
            return "", ""
