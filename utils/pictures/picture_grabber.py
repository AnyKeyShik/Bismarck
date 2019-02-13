# -*- coding: utf-8 -*-

from core import PictureNotFoundException

from utils.logger import class_construct, log_func, info, debug

from .konachan_grabber import KonachanGrabber as KonaGrabber
from .yandere_grabber import YandereGrabber as YandeGrabber


class PictureGrabber(object):
    """
    Unified grabber for konachan and yandere
    """

    _kon = None
    _ya = None

    @class_construct
    def __init__(self):
        self._kon = KonaGrabber()
        self._ya = YandeGrabber()

    @log_func()
    def get_picture(self, tags, rating):
        """
        Get picture

        :param tags: picture tags
        :param rating: picture rating
        :return: picture url and hash
        :rtype: (str, str)
        :raise: PictureNotFoundException if picture not found
        """

        info("PictureGrabber get_picture()")
        url, picture_hash = self._kon.get_picture(tags, rating)
        debug("Get url '" + str(url) + "' and hash '" + str(picture_hash) + "'")

        if picture_hash != "":
            info("Found picture in Konachan. Returning")
            return url, picture_hash
        else:
            info("Not found picture in Konachan. Continue")

            url, picture_hash = self._ya.get_picture(tags, rating)
            debug("Get url '" + str(url) + "' and hash '" + str(picture_hash) + "'")

            if picture_hash != "":
                info("Found picture in Yandere. Returning")
                return url, picture_hash
            else:
                info("Not found picture in Yandere. Raise PictureNotFoundException")
                raise PictureNotFoundException
