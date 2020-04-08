# -*- coding: utf-8 -*-

#   Copyright (c) 2020.
#  #
#   Created by AnyKeyShik Rarity
#  #
#   Telegram: @AnyKeyShik
#   GitHub: https://github.com/AnyKeyShik
#   E-mail: nikitav59@gmail.com

import socket

import socks

from . import logger


@logger.log_func
def create_connection(address):
    """
    Create connection with custom sock

    :param address: address for connection
    :return: connection sock
    :rtype: socks.socksocket
    """

    sock = socks.socksocket()
    sock.connect(address)
    return sock


@logger.log_func
def config(ip, port):
    """
    Config proxy

    :param ip: proxy ip
    :param port: proxy port
    :return: None
    :rtype: None
    """

    socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, ip, port)


@logger.log_func
def patch():
    """
    Patch the socket module

    :return: None
    :rtype: None
    """

    config("127.0.0.1", 9050)

    socket.socket = socks.socksocket
    socket.create_connection = create_connection
