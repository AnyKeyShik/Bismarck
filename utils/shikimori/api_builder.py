# -*- coding: utf-8 -*-

import urllib.parse
from time import sleep

import requests

from core import TooManyRequestsException, UnexpectedCodeException


def retry_on_error(retries_count=3, delay=0.1):
    def decorator(func):
        def new_func(*args, **kwargs):
            for try_count in range(retries_count):
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
        self._path = base
        self._headers = headers

    def _getattr_(self, name):
        self._path = urllib.parse.urljoin(self._path + "/", name)
        return self

    def _getitem_(self, item):
        return self._getattr_(str(item))

    @retry_on_error()
    def get(self, **kwargs):
        r = requests.get(self._path, params=kwargs, headers=self._headers)
        raise_exception_by_code(r.status_code)
        return r.text

    @retry_on_error()
    def post(self, **kwargs):
        r = requests.post(self._path, data=kwargs)
        raise_exception_by_code(r.status_code)
        return r.text


class ApiBuilder(object):
    def __init__(self, server, headers=None):
        self._server = server
        self._headers = headers

    def _getattr_(self, name):
        ap = ApiPath(self._server, self._headers)
        return ap._getattr_(name)

    def _getitem_(self, item):
        self._getattr_(str(item))
