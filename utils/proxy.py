# -*- coding: utf-8 -*-

import socket

import socks

from utils.logger import DEBUG_LOG, log_func


@log_func(log_write=DEBUG_LOG)
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


@log_func(log_write=DEBUG_LOG)
def config(ip, port):
    """
    Config tor-proxy

    :param ip: proxy ip
    :param port: proxy port
    :return: None
    :rtype: None
    """

    socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, ip, port)


@log_func(log_write=DEBUG_LOG)
def patch():
    """
    Patch the socket module

    :return: None
    :rtype: None
    """

    config("127.0.0.1", 9050)

    socket.socket = socks.socksocket
    socket.create_connection = create_connection
