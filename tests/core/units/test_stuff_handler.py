# -*- coding: utf-8 -*-

import unittest

from core import TagNotFoundException, CommandNotFoundException, RatingNotFoundException
from core.utils.json_handler import json_handler


class TestStuffHandler(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Init tests...\n" + "=" * 50 + "\n")

    def test_commands(self):
        print("Start commands test in StuffHandler")

        self.assertEqual("что скажешь про", json_handler.commands[0])
        self.assertNotEqual("что думаешь об", json_handler.commands[3])

        print("Commands test in StuffHandler passed successfully!")

    def test_commands_parts(self):
        print("Start commands parts test in StuffHandler")

        self.assertEqual("скажешь", json_handler.commands_parts[1])
        self.assertEqual("расскажи", json_handler.commands_parts[3])
        self.assertEqual(9, len(json_handler.commands_parts))

        print("Commands parts test in StuffHandler passed successfully!")

    def test_command_present(self):
        print("Start command present test in StuffHandler")

        self.assertEqual("hello", json_handler.command_present("хай"))
        with self.assertRaises(CommandNotFoundException):
            json_handler.command_present("школьница")

        print("Command present test in StuffHandler passed successfully!")

    def test_tag(self):
        print("Start tags test in StuffHandler")

        self.assertEqual("брюнетка", json_handler.tags[0])
        self.assertNotEqual("кошкодевочка", json_handler.tags[3])

        print("Tags test in StuffHandler passed successfully!")

    def test_tags_parts(self):
        print("Start tags parts test in StuffHandler")

        self.assertEqual("длинные", json_handler.tags_parts[0])
        self.assertNotEqual("девочка", json_handler.tags_parts[3])

        print("Tags parts test in StuffHandler passed successfully!")

    def test_tag_present(self):
        print("Start tag present test in StuffHandler")

        self.assertEqual("blush", json_handler.tag_present("румянец"))
        with self.assertRaises(TagNotFoundException):
            json_handler.tag_present("этти")

        print("Tag present test in StuffHandler passed successfully!")

    def test_ratings(self):
        print("Start ratings test in StuffHandler")

        self.assertEqual("хентай", json_handler.ratings[0])
        self.assertNotEqual("", json_handler.tags[2])

        print("Ratings test in StuffHandler passed successfully!")

    def test_rating_present(self):
        print("Start rating present test in StuffHandler")

        self.assertEqual("questionable", json_handler.rating_present("этти"))
        with self.assertRaises(RatingNotFoundException):
            json_handler.rating_present("лоли")

        print("Rating present test in StuffHandler passed successfully!")
