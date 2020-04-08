# -*- coding: utf-8 -*-

#   Copyright (c) 2020.
#  #
#   Created by AnyKeyShik Rarity
#  #
#   Telegram: @AnyKeyShik
#   GitHub: https://github.com/AnyKeyShik
#   E-mail: nikitag594@gmail.com

from json.decoder import JSONDecodeError

import requests

from core.utils import logger


class Grabber(object):
    _url = ""

    @logger.log_func
    def get_picture(self, tags, rating):
        """
        Get picture with tag and rating

        :param tags: tags of picture
        :param rating: picture rating
        :return: picture url and hash or empty strings
        :rtype: (str, str)
        """
        logger.info("get_picture()")

        url = self._url % (tags, rating)

        logger.debug("Get url: " + str(url))

        try:
            picture_object = requests.get(url).json()
        except ConnectionError:
            logger.info("Return empty strings: connection error")
            return "", ""
        except JSONDecodeError:
            logger.info("Picture not found")
            return "", ""

        logger.debug("Get picture: " + str(picture_object))

        try:
            logger.info("Try to return picture link and hash")
            return picture_object[0]['file_url'], picture_object[0]['md5']

        except Exception:
            logger.info("Return empty strings: picture not found")
            return "", ""
