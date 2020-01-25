# -*- coding: utf-8 -*-

import re

from fuzzywuzzy import fuzz

from core.logger import log_func, debug, DEBUG_LOG

TAG = "StringProcessor"


def is_words_similar(string, model):
    """
    Calculates the Levenshtein distance between two strings

    :param string: user input
    :param model: model string
    :return: Is words are similar
    :rtype: bool
    """

    if fuzz.ratio(string, model) >= 75:
        return True

    return False


@log_func(log_write=DEBUG_LOG)
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
    debug(TAG, "Split message: " + str(split_message))

    message = []
    for msg in [x.split("-") for x in split_message]:
        for i in msg:
            if i != "":
                message.append(i)

    return message
