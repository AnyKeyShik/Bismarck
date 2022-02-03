# -*- coding: utf-8 -*-

#   Copyright (c) 2020.
#
#   Created by AnyKeyShik Rarity
#
#   Telegram: @AnyKeyShik
#   GitHub: https://github.com/AnyKeyShik
#   E-mail: nikitag594@gmail.com

class NotFoundException(Exception):
    pass


class AnimeNotFoundException(NotFoundException):
    pass


class CommandNotFoundException(NotFoundException):
    pass


class PictureNotFoundException(NotFoundException):
    pass


class RatingNotFoundException(NotFoundException):
    pass


class TagsNotFoundException(NotFoundException):
    pass


class TagNotFoundException(NotFoundException):
    pass


class DeniedException(Exception):
    pass


class HentaiDeniedException(DeniedException):
    pass


class EcchiDeniedException(DeniedException):
    pass


class ErrorException(Exception):
    pass


class DownloadErrorException(ErrorException):
    pass


class TooManyRequestsException(ErrorException):
    pass


class UnexpectedCodeException(ErrorException):
    pass
