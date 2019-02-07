# -*- coding: utf-8 -*-

import unittest
from anytree import RenderTree

from utils.text_processor.string_processor import StringProcessor


class TestStringProcessor(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Init tests...\n" + "=" * 50 + "\n")

        cls.sp = StringProcessor()
        cls.sp.create_message_tree(",,,,,,ЮОИ некопара. что    скажешь про      SAO?              "
                                   "И покажи хентай!!!! с лолями!!!!!!!!!!-школьницами")

    @classmethod
    def tearDownClass(cls):
        print("\nFinish getters tests!\n")

        tree = cls.sp.get_tree()

        for pre, fill, node in RenderTree(tree):
            print("%s%s" % (pre, node.name))

        print("=" * 50 + "\nFinish tests!")

    def test_tag(self):
        print("def get_tag() test")\

        self.assertEqual(['юри', 'некопара', 'лоли', 'школьница'], self.sp.get_tags())

        print("def get_tag() test passed successfully!")

    def test_rating(self):
        print("def get_rating() test")

        self.assertEqual("хентай", self.sp.get_rating())

        print("def get_rating() test passed successfully!")

    def test_command(self):
        print("def get_commands() test")

        self.assertEqual(['что скажешь про'], self.sp.get_commands())

        print("def get_commands() test passed successfully!")
