# -*- coding: utf-8 -*-

import requests

from core import PictureNotFoundException
from utils.json_handler import JsonHandler
from utils.logger import class_construct, log_func, info, debug
from .konachan_grabber import KonachanGrabber as KonaGrabber
from .yandere_grabber import YandereGrabber as YandeGrabber


class PictureGrabber(object):
    """
    Unified grabber for konachan and yandere
    """

    _kon = None
    _ya = None
    _handler = None

    @class_construct
    def __init__(self):
        self._kon = KonaGrabber()
        self._ya = YandeGrabber()

        self._handler = JsonHandler()

    @log_func()
    def get_picture(self, tags, rating):
        """
        Get picture

        :param tags: picture tags
        :param rating: picture rating
        :raise: PictureNotFoundException if picture not found
        """

        info("PictureGrabber get_picture()")

        debug("Join tags list by '+'")
        if type(tags) == list:
            tags = '+'.join(tags)

        url, picture_hash = self._kon.get_picture(tags, rating)
        debug("Get url '" + str(url) + "' and hash '" + str(picture_hash) + "'")

        if picture_hash != "":
            info("Found picture in Konachan. Returning")

            self._download_picture(url)

        else:
            info("Not found picture in Konachan. Continue")

            url, picture_hash = self._ya.get_picture(tags, rating)
            debug("Get url '" + str(url) + "' and hash '" + str(picture_hash) + "'")

            if picture_hash != "":
                info("Found picture in Yandere. Returning")

                self._download_picture(url)
            else:
                info("Not found picture in Yandere. Raise PictureNotFoundException")
                raise PictureNotFoundException()

    @log_func()
    def _download_picture(self, url):
        """
        Download picture as file from url

        :param url: url for downloading
        :raise: PictureNotFoundException if error occurring while downloading
        """
        try:
            raw_picture = requests.get(url)
            picture = open(self._handler.constants['default_picture_file'], 'wb')
            for chunk in raw_picture.iter_content(chunk_size=512 * 1024):
                if chunk:
                    picture.write(chunk)
            picture.close()

        except:
            raise PictureNotFoundException()
