# -*- coding: utf-8 -*-

import unittest

from utils.text_processor.utils import distance, prepare_msg


class TestStringUtils(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Init tests...\n" + "=" * 50 + "\n")

    def test_distance(self):
        print("def distance() test")

        self.assertEqual(1, distance("юои", "юри"))
        self.assertEqual(2, distance("простая проверка", "поостая провекка"))
        self.assertNotEqual(0, distance("хентай", "хннтай"))

        print("def distance() test passed successfully!")

    def test_prepare_msg(self):
        print("def prepare_msg() test")

        msg = prepare_msg(",,,,,,ЮОИ некопара. что    скажешь про      SAO?              "
                          "И покажи хентай!!!! с лолями!!!!!!!!!!-школьницами")
        self.assertEqual(['юои', 'некопара', 'что', 'скажешь', 'про', 'sao', 'и', 'покажи', 'хентай', 'с',
                          'лолями', 'школьницами'], msg)

        msg = prepare_msg("[id336383265|*bismarkb1996], i hate this fcking shit!!!!!!!")
        self.assertEqual(['i', 'hate', 'this', 'fcking', 'shit'], msg)

        print("def prepare_msg() test passed successfully!")
