# -*- coding: utf-8 -*-

import re

from utils.logger import log_func, debug, DEBUG_LOG


@log_func(log_write=DEBUG_LOG)
def distance(string, model):
    """
    Calculates the Levenshtein distance between two strings

    :param string: user input
    :param model: model string
    :return: Levenshtein distance
    :rtype: int
    """
    n, m = len(string), len(model)

    if n > m:
        string, model = model, string
        n, m = m, n

    current_column = range(n + 1)

    for i in range(1, m + 1):
        previous_column, current_column = current_column, [i] + [0] * n

        for j in range(1, n + 1):
            add, delete, change = previous_column[j] + 1, current_column[j - 1] + 1, previous_column[j - 1]

            if string[j - 1] != model[i - 1]:
                change += 1

            current_column[j] = min(add, delete, change)

    return current_column[n]


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
    debug("Lower message: " + raw_message)
    raw_message = raw_message.replace("*bismarkb1996", "@bismarkb1996")
    debug("Replace appeal: " + raw_message)
    raw_message = raw_message.replace(",", " ")
    raw_message = raw_message.replace("!", " ")
    raw_message = raw_message.replace("?", " ")
    raw_message = raw_message.replace(".", "")
    debug("Remove marks: " + raw_message)
    raw_message = raw_message.replace("[id336383265|@bismarkb1996] ", "")
    debug("Remove appeal: " + raw_message)
    raw_message = re.sub(' +', ' ', raw_message)
    debug("Remove extra spaces: " + raw_message)

    split_message = raw_message.split(" ")
    debug("Split message: " + str(split_message))

    message = []
    for msg in [x.split("-") for x in split_message]:
        for i in msg:
            if i != "":
                message.append(i)

    return message
