# -*- coding: utf-8 -*-

import json
import unittest

import pkg_resources
from anytree import RenderTree

from core.text_processor import StringProcessor


class TestStringProcessor(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Init tests...\n" + "=" * 50 + "\n")

        resource_path = '/'.join(('../snippets', 'input.json'))
        template = pkg_resources.resource_stream(__name__, resource_path)
        line = template.read().decode('utf-8')
        input_string = json.loads(line)['messages']['string_processor']
        template.close()

        cls.sp = StringProcessor()
        cls.sp.create_message_tree(input_string)

        resource_path = '/'.join(('../snippets', 'model.json'))
        template = pkg_resources.resource_stream(__name__, resource_path)
        line = template.read().decode('utf-8')
        cls.tags = json.loads(line)['string_processor']['tags']
        cls.rating = json.loads(line)['string_processor']['rating']
        cls.commands = json.loads(line)['string_processor']['commands']
        template.close()

    @classmethod
    def tearDownClass(cls):
        print("\nFinish getters tests!\n")

        tree = cls.sp.get_tree()

        for pre, fill, node in RenderTree(tree):
            print("%s%s" % (pre, node.name))

        print("=" * 50 + "\nFinish tests!")

    def test_tag(self):
        print("Start tags test in StringProcessor")

        self.assertEqual(self.tags, self.sp.get_tags())

        print("Tags test in StringProcessor passed successfully!")

    def test_rating(self):
        print("Start rating test in StringProcessor")

        self.assertEqual(self.rating, self.sp.get_rating())

        print("Rating test in StringProcessor passed successfully!")

    def test_command(self):
        print("Start commands test in StringProcessor")

        self.assertEqual(self.commands, self.sp.get_commands())

        print("Commands test in StringProcessor passed successfully!")
