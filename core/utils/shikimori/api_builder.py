# -*- coding: utf-8 -*-

#   Copyright (c) 2020.
#
#   Created by AnyKeyShik Rarity
#
#   Telegram: @AnyKeyShik
#   GitHub: https://github.com/AnyKeyShik
#   E-mail: nikitag594@gmail.com

import urllib.parse
from time import sleep

import requests


class TooManyRequestsException(Exception):
    pass


class UnexpectedCodeException(Exception):
    pass


def retry_on_error(retries_count=3, delay=0.1):
    def decorator(func):
        def new_func(*args, **kwargs):
            for _ in range(retries_count):
                try:
                    return func(*args, **kwargs)
                except TooManyRequestsException:
                    sleep(delay)
            return func(*args, **kwargs)
        return new_func
    return decorator


def raise_exception_by_code(code):
    if code == 429:
        raise TooManyRequestsException()
    if code != 200:
        raise UnexpectedCodeException()


class ApiPath(object):
    def __init__(self, base, headers):
        self.__path = base
        self.__headers = headers

    def __getattr__(self, name):
        self.__path = urllib.parse.urljoin(self.__path + "/", name)
        return self

    def __getitem__(self, item):
        return self.__getattr__(str(item))

    @retry_on_error()
    def get(self, **kwargs):
        r = requests.get(self.__path, params=kwargs, headers=self.__headers)
        raise_exception_by_code(r.status_code)
        return r.text

    @retry_on_error()
    def post(self, **kwargs):
        r = requests.post(self.__path, data=kwargs)
        raise_exception_by_code(r.status_code)
        return r.text


class ApiBuilder(object):
    def __init__(self, server, headers=None):
        self.__server = server
        self.__headers = headers

    def __getattr__(self, name):
        ap = ApiPath(self.__server, self.__headers)
        return ap.__getattr__(name)

    def __getitem__(self, item):
        self.__getattr__(str(item))
