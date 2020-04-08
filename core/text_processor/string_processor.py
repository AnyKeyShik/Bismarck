# -*- coding: utf-8 -*-

#   Copyright (c) 2020.
#  #
#   Created by AnyKeyShik Rarity
#  #
#   Telegram: @AnyKeyShik
#   GitHub: https://github.com/AnyKeyShik
#   E-mail: nikitag594@gmail.com

#   Copyright (c) 2020.
#  #
#   Created by AnyKeyShik Rarity
#  #
#   Telegram: @AnyKeyShik
#   GitHub: https://github.com/AnyKeyShik
#   E-mail: nikitag594@gmail.com

import re

from rapidfuzz import fuzz

from . import logger


def is_words_similar(string, model):
    """
    Calculates the Levenshtein distance between two strings

    :param string: user input
    :param model: model string
    :return: Is words are similar
    :rtype: bool
    """

    if fuzz.ratio(string, model, score_cutoff=75, preprocess=False):
        return True

    return False


@logger.log_func
def prepare_msg(raw_message):
    """
    Prepare user message for processing

    :param raw_message: raw user message
    :return: prepared and split user message
    :rtype: list
    """

    raw_message = str(raw_message)

    raw_message = raw_message.lower()
    raw_message = raw_message.replace("bismarkb1996", "")
    raw_message = raw_message.replace("id336383265", "")
    raw_message = re.sub('[^а-яА-Яa-zA-Z0-9\\s\\-]+', '', raw_message)

    split_message = raw_message.split(" ")
    logger.debug("Split message: " + str(split_message))

    message = []
    for msg in [x.split("-") for x in split_message]:
        for i in msg:
            if i != "":
                message.append(i)

    return message
