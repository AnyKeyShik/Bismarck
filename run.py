# -*- coding: utf-8 -*-

from argparse import ArgumentParser

from core import Kernel
from social import VkHandler

parser = ArgumentParser(description="Bot for MSU Anime Club")
parser.add_argument("-l", "--local", help="Run bot locale", action='store_true')
parser.add_argument("-d", "--deploy", help="For deploy bot on server", action='store_true')

if __name__ == "__main__":
    args = parser.parse_args()

    if args.deploy:
        VK = VkHandler()
        VK.handler()
    else:
        kernel = Kernel()

        while 1:
            print(">", end=" ")
            message = str(input())

            print(kernel.talk(message, True))
