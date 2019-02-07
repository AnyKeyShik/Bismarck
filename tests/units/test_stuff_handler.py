# -*- coding: utf-8 -*-

import unittest

from utils.stuff_handler import StuffHandler
from exceptions import TagNotFoundException, CommandNotFoundException, RatingNotFoundException


class TestStuffHandler(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Init tests...\n" + "=" * 50 + "\n")

        cls.handler = StuffHandler()

    def test_commands(self):
        print("Test def commands()")

        self.assertEqual("что скажешь про", self.handler.commands[0])
        self.assertNotEqual("что думаешь об", self.handler.commands[3])

        print("Test def commands() passed successfully!")

    def test_commands_parts(self):
        print("Test def commands_parts()")

        self.assertEqual("скажешь", self.handler.commands_parts[1])
        self.assertEqual("расскажи", self.handler.commands_parts[3])
        with self.assertRaises(IndexError):
            self.handler.commands_parts[7] # Test for part "об"

        print("Test def commands_parts() passed successfully!")

    def test_command_present(self):
        print("Test def command_present()")

        self.assertEqual("hello", self.handler.command_present("хай"))
        with self.assertRaises(CommandNotFoundException):
            self.handler.command_present("школьница")

        print("Test def command_present() passed successfully!")

    def test_tag(self):
        print("Test def tags()")

        self.assertEqual("брюнетка", self.handler.tags[0])
        self.assertNotEqual("кошкодевочка", self.handler.tags[3])

        print("Test def tags() passed successfully!")

    def test_tags_parts(self):
        print("Test def tags_parts()")

        self.assertEqual("алые", self.handler.tags_parts[0])
        self.assertNotEqual("девочка", self.handler.tags_parts[3])

        print("Test def tags_parts() passed successfully!")

    def test_tag_present(self):
        print("Test def tag_present()")

        self.assertEqual("blush", self.handler.tag_present("румянец"))
        with self.assertRaises(TagNotFoundException):
            self.handler.tag_present("этти")

        print("Test def tag_present() passed successfully!")

    def test_ratings(self):
        print("Test def ratings()")

        self.assertEqual("хентай", self.handler.ratings[0])
        self.assertNotEqual("", self.handler.tags[2])

        print("Test def rating() passed successfully!")

    def test_rating_present(self):
        print("Test def rating_present()")

        self.assertEqual("questionable", self.handler.rating_present("этти"))
        with self.assertRaises(RatingNotFoundException):
            self.handler.rating_present("лоли")

        print("Test def rating_present() passed successfully!")
