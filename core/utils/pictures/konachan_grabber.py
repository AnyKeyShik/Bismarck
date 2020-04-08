# -*- coding: utf-8 -*-

#   Copyright (c) 2020.
#  #
#   Created by AnyKeyShik Rarity
#  #
#   Telegram: @AnyKeyShik
#   GitHub: https://github.com/AnyKeyShik
#   E-mail: nikitag594@gmail.com

#   Copyright (c) 2020.
#  #
#   Created by AnyKeyShik Rarity
#  #
#   Telegram: @AnyKeyShik
#   GitHub: https://github.com/AnyKeyShik
#   E-mail: nikitag594@gmail.com

from core.utils import logger
from .grabber import Grabber


class KonachanGrabber(Grabber):
    """
    Grabber picture for http://konachan.com/
    """

    _url = None

    @logger.class_construct
    def __init__(self):
        self._url = "http://konachan.com/post.json?tags=%s+rating:%s+order:random&limit=1"
