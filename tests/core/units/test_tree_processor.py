# -*- coding: utf-8 -*-

import json
import unittest

import pkg_resources
from anytree import RenderTree

from core.text_processor import TreeProcessor


class TestTreeProcessor(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Init tests...\n" + "=" * 50 + "\n")

        resource_path = '/'.join(('../snippets', 'input.json'))
        template = pkg_resources.resource_stream(__name__, resource_path)
        line = template.read().decode('utf-8')
        input_string = json.loads(line)['messages']['tree_processor']
        template.close()

        cls.sp = TreeProcessor()
        cls.sp.create_message_tree(input_string)
        cls.sp.parse_message_tree()

        resource_path = '/'.join(('../snippets', 'model.json'))
        template = pkg_resources.resource_stream(__name__, resource_path)
        line = template.read().decode('utf-8')
        cls.tags = json.loads(line)['tree_processor']['tags']
        cls.rating = json.loads(line)['tree_processor']['rating']
        cls.commands = json.loads(line)['tree_processor']['commands']
        cls.argument = json.loads(line)['tree_processor']['argument']
        template.close()

    @classmethod
    def tearDownClass(cls):
        print("\nFinish getters tests!\n")

        tree = cls.sp.get_tree()

        for pre, _, node in RenderTree(tree):
            print("%s%s" % (pre, node.name))

        print("=" * 50 + "\nFinish tests!")

    def test_tag(self):
        print("Start tags test in TreeProcessor")

        self.assertEqual(self.tags, self.sp.get_tags())

        print("Tags test in TreeProcessor passed successfully!")

    def test_rating(self):
        print("Start rating test in TreeProcessor")

        self.assertEqual(self.rating, self.sp.get_rating())

        print("Rating test in TreeProcessor passed successfully!")

    def test_command(self):
        print("Start commands test in TreeProcessor")

        command, arg = self.sp.get_commands()
        self.assertEqual(self.commands, command)
        self.assertEqual(self.argument, arg)

        print("Commands test in TreeProcessor passed successfully!")
