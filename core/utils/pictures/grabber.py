# -*- coding: utf-8 -*-

from json.decoder import JSONDecodeError

import requests

from core.utils.logger import log_func, debug, info, DEBUG_LOG


class Grabber(object):
    _url = ""
    _TAG = "Grabber"

    @log_func(log_write=DEBUG_LOG)
    def get_picture(self, tags, rating):
        """
        Get picture with tag and rating

        :param tags: tags of picture
        :param rating: picture rating
        :return: picture url and hash or empty strings
        :rtype: (str, str)
        """
        info(self._TAG, "get_picture()")

        url = self._url % (tags, rating)

        debug(self._TAG, "Get url: " + str(url))

        try:
            picture_object = requests.get(url).json()
        except ConnectionError:
            info(self._TAG, "Return empty strings: connection error")
            return "", ""
        except JSONDecodeError:
            info(self._TAG, "Picture not found")
            return "", ""

        debug(self._TAG, "Get picture: " + str(picture_object))

        try:
            info(self._TAG, "Try to return picture link and hash")
            return picture_object[0]['file_url'], picture_object[0]['md5']

        except Exception:
            info(self._TAG, "Return empty strings: picture not found")
            return "", ""
