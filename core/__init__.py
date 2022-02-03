# -*- coding: utf-8 -*-

#   Copyright (c) 2020.
#
#   Created by AnyKeyShik Rarity
#
#   Telegram: @AnyKeyShik
#   GitHub: https://github.com/AnyKeyShik
#   E-mail: nikitag594@gmail.com

import datetime
import logging.config
import os

import yaml

_base_dir = os.path.join(os.path.dirname(__file__), os.environ['BISMARCK_HOME'] + os.sep + "logs")
_dir_name = str(datetime.datetime.now().strftime("%Y_%m_%d_%H-%M-%S"))
_logs_dir = os.path.join(_base_dir, _dir_name)

try:
    os.mkdir(_logs_dir)
except Exception:
    exit(255)

_logs_level = os.environ['BISMARCK_LOGLEVEL']
_module_names = ['command_processor', 'text_processor', 'utils', 'kernel', 'social']

_log_config = yaml.safe_load(open(os.path.join(os.environ['BISMARCK_HOME'], "log_config.yaml")))
_log_config["handlers"]["root"]["filename"] = _log_config["handlers"]["root"]["filename"].format(path=_logs_dir)
for module_name in _module_names:
    _log_config["handlers"][module_name]["filename"] = _log_config["handlers"][module_name]["filename"].format(
        path=_logs_dir, name=(module_name))
    _log_config["loggers"][module_name]["level"] = _log_config["loggers"][module_name]["level"].format(
        level=_logs_level)
logging.config.dictConfig(_log_config)

from .logger import Logger

logger = Logger("kernel")

from .command_processor import CommandProcessor
from .kernel import Kernel
from .text_processor import TreeProcessor
