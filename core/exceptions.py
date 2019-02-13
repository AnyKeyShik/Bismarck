# -*- coding: utf-8 -*-


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


class TagNotFoundException(NotFoundException):
    pass


class TooManyRequestsException(Exception):
    pass


class UnexpectedCodeException(Exception):
    pass
