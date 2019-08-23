# -*- coding: utf-8 -*-

from utils.logger import class_construct
from .grabber import Grabber


class YandereGrabber(Grabber):
    """
    Picture grabber for http://yande.re/
    """

    _url = None

    @class_construct
    def __init__(self):
        self._url = "https://yande.re/post.json?tags=%s+rating:%s+order:random&limit=1"
