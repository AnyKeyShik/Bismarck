# -*- coding: utf-8 -*-

from utils.logger import class_construct
from .grabber import Grabber


class KonachanGrabber(Grabber):
    """
    Grabber picture for http://konachan.com/
    """

    _url = None

    @class_construct
    def __init__(self):
        self._url = "http://konachan.com/post.json?tags=%s+rating:%s+order:random&limit=1"
