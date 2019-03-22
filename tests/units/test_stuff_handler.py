# -*- coding: utf-8 -*-

import unittest

from core import TagNotFoundException, CommandNotFoundException, RatingNotFoundException
from utils.json_handler import JsonHandler


class TestStuffHandler(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Init tests...\n" + "=" * 50 + "\n")

        cls.handler = JsonHandler()

    def test_commands(self):
        print("Start commands test in StuffHandler")

        self.assertEqual("что скажешь про", self.handler.commands[0])
        self.assertNotEqual("что думаешь об", self.handler.commands[3])

        print("Commands test in StuffHandler passed successfully!")

    def test_commands_parts(self):
        print("Start commands parts test in StuffHandler")

        self.assertEqual("скажешь", self.handler.commands_parts[1])
        self.assertEqual("расскажи", self.handler.commands_parts[3])
        self.assertEqual(9, len(self.handler.commands_parts))

        print("Commands parts test in StuffHandler passed successfully!")

    def test_command_present(self):
        print("Start command present test in StuffHandler")

        self.assertEqual("hello", self.handler.command_present("хай"))
        with self.assertRaises(CommandNotFoundException):
            self.handler.command_present("школьница")

        print("Command present test in StuffHandler passed successfully!")

    def test_tag(self):
        print("Start tags test in StuffHandler")

        self.assertEqual("брюнетка", self.handler.tags[0])
        self.assertNotEqual("кошкодевочка", self.handler.tags[3])

        print("Tags test in StuffHandler passed successfully!")

    def test_tags_parts(self):
        print("Start tags parts test in StuffHandler")

        self.assertEqual("алые", self.handler.tags_parts[0])
        self.assertNotEqual("девочка", self.handler.tags_parts[3])

        print("Tags parts test in StuffHandler passed successfully!")

    def test_tag_present(self):
        print("Start tag present test in StuffHandler")

        self.assertEqual("blush", self.handler.tag_present("румянец"))
        with self.assertRaises(TagNotFoundException):
            self.handler.tag_present("этти")

        print("Tag present test in StuffHandler passed successfully!")

    def test_ratings(self):
        print("Start ratings test in StuffHandler")

        self.assertEqual("хентай", self.handler.ratings[0])
        self.assertNotEqual("", self.handler.tags[2])

        print("Ratings test in StuffHandler passed successfully!")

    def test_rating_present(self):
        print("Start rating present test in StuffHandler")

        self.assertEqual("questionable", self.handler.rating_present("этти"))
        with self.assertRaises(RatingNotFoundException):
            self.handler.rating_present("лоли")

        print("Rating present test in StuffHandler passed successfully!")
