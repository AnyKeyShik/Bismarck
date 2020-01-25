# -*- coding: utf-8 -*-

import os

import requests

from core.exceptions import PictureNotFoundException, TagsNotFoundException, EcchiDeniedException, \
    HentaiDeniedException, DownloadErrorException
from core.utils.json_handler import json_handler
from core.utils.logger import class_construct, log_func, info, debug
from .konachan_grabber import KonachanGrabber as KonaGrabber
from .yandere_grabber import YandereGrabber as YandeGrabber


class PictureGrabber(object):
    """
    Unified grabber for konachan and yandere
    """

    _kon = None
    _ya = None

    _TAG = "PictureGrabber"

    @class_construct
    def __init__(self):
        self._kon = KonaGrabber()
        self._ya = YandeGrabber()

    @log_func()
    def get_picture(self, tags, rating, from_user):
        """
        Get picture

        :param tags: picture tags
        :param rating: picture rating
        :param from_user: type of chat message from
        :raise: PictureNotFoundException if picture not found
        :raise: TagsNotFoundException if request picture without tags
        :raise: EcchiDeniedException if request ecchi in non private chat
        :raise: HentaiDeniedException if request hentai on non private chat
        :rtype: None
        """

        info(self._TAG, "PictureGrabber get_picture()")

        if (not from_user) and rating != "safe":
            if rating == "questionable":
                info(self._TAG, "Request ecchi in non private chat. Denied. Current rating: '" + str(rating) + "'")
                raise EcchiDeniedException
            else:
                info(self._TAG, "Request hentai on non private chat. Denied. Current rating: '" + str(rating) + "'")
                raise HentaiDeniedException

        debug(self._TAG, "Join tags list by '+'")
        if isinstance(tags, list):
            if len(tags) != 0:
                tags = '+'.join(tags)
                info(self._TAG, "Tags in request: '" + str(tags) + "'")
            else:
                info(self._TAG, "Not found tags in request. Raise TagsNotFoundException")
                raise TagsNotFoundException

        url, picture_hash = self._kon.get_picture(tags, rating)
        debug(self._TAG, "Get url '" + str(url) + "' and hash '" + str(picture_hash) + "'")

        if picture_hash != "":
            info(self._TAG, "Found picture in Konachan. Returning")

            self._download_picture(url)

        else:
            info(self._TAG, "Not found picture in Konachan. Continue")

            url, picture_hash = self._ya.get_picture(tags, rating)
            debug(self._TAG, "Get url '" + str(url) + "' and hash '" + str(picture_hash) + "'")

            if picture_hash != "":
                info(self._TAG, "Found picture in Yandere. Returning")

                self._download_picture(url)
            else:
                info(self._TAG, "Not found picture in Yandere. Raise PictureNotFoundException")
                raise PictureNotFoundException()

    @log_func()
    def _download_picture(self, url):
        """
        Download picture as file from url

        :param url: url for downloading
        :raise: PictureNotFoundException if error occurring while downloading
        :rtype: None
        """
        try:
            raw_picture = requests.get(url)
            picture = open("pictures" + os.path.sep + json_handler.constants['default_picture_file'], 'wb')
            for chunk in raw_picture.iter_content(chunk_size=512 * 1024):
                if chunk:
                    picture.write(chunk)
            picture.close()

        except Exception as e:
            debug(self._TAG, "Error download with exception: " + str(e))
            raise DownloadErrorException()
