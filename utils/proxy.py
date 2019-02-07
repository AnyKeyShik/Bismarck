# -*- coding: utf-8 -*-

import socks
import socket


def create_connection(address):
    r"""
    Create connection with custom sock

    :param address: address for connection
    :return: connection sock
    """

    sock = socks.socksocket()
    sock.connect(address)
    return sock


# Config tor-proxy
socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9050)

# Patch the socket module
socket.socket = socks.socksocket
socket.create_connection = create_connection