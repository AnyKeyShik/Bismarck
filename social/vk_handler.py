# -*- coding: utf-8 -*-

#   Copyright (c) 2020.
#  #
#   Created by AnyKeyShik Rarity
#  #
#   Telegram: @AnyKeyShik
#   GitHub: https://github.com/AnyKeyShik
#   E-mail: nikitag594@gmail.com

import os
from random import randint

from vk_api import VkApi
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.upload import VkUpload

from core import Kernel
from core.utils.json_handler import json_handler
from . import logger


class VkHandler(object):
    _auth_consts = None
    _vk_session = None
    _vk_api = None
    _vk_upload = None

    _kernel = None
    _picture_dir = None

    @logger.class_construct
    def __init__(self):
        self._auth_consts = json_handler.auth_constants
        self._vk_session = VkApi(token=self._auth_consts['api_token'], app_id=self._auth_consts['app_id'],
                                 client_secret=self._auth_consts['client_secret'])
        self._vk_api = self._vk_session.get_api()
        self._vk_upload = VkUpload(self._vk_session)
        self._kernel = Kernel()
        self._picture_dir = os.environ['BISMARCK_HOME'] + os.sep + "pictures" + os.sep

    def handler(self):
        longpoll = VkLongPoll(self._vk_session)
        for event in longpoll.listen():

            if event.type == VkEventType.MESSAGE_NEW:
                logger.debug("New message: '" + str(event.text) + "'")

                if (event.from_user and not event.from_me) or \
                        (event.from_chat and event.text.find('id336383265') != -1) or event.from_group:
                    logger.info("New message: '" + str(event.text) + "'")

                    answer = self._kernel.talk(str(event.text), event.from_user)

                    if event.from_user:
                        peer_id = event.user_id
                    elif event.from_chat:
                        peer_id = 2000000000 + event.chat_id
                    else:
                        peer_id = 0 - event.group_id

                    if isinstance(answer, tuple):
                        message, picture = answer
                        picture = self._picture_dir + picture
                        picture_id = self._vk_upload.photo_messages(photos=picture)
                        attachment = "photo{}_{}".format(picture_id[0]['owner_id'], picture_id[0]['id'])
                        self._vk_api.messages.send(
                            peer_id=peer_id,
                            message=message,
                            random_id=randint(0, 1000000000000000),
                            attachment=attachment
                        )
                    else:
                        self._vk_api.messages.send(
                            peer_id=peer_id,
                            message=answer,
                            random_id=randint(0, 1000000000000000)
                        )
