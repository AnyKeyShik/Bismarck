# -*- coding: utf-8 -*-

import json
import unittest

import pkg_resources

from core.text_processor.string_processor import is_words_similar, prepare_msg


class TestStringUtils(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Init tests...\n" + "=" * 50 + "\n")

        resource_path = '/'.join(('../snippets', 'input.json'))
        template = pkg_resources.resource_stream(__name__, resource_path)
        line = template.read().decode('utf-8')
        cls.input_sp = json.loads(line)['messages']['tree_processor']
        cls.input_su = json.loads(line)['messages']['string_processor']
        template.close()

        resource_path = '/'.join(('../snippets', 'model.json'))
        template = pkg_resources.resource_stream(__name__, resource_path)
        line = template.read().decode('utf-8')
        cls.sp = json.loads(line)['string_processor']['tree_processor']
        cls.su = json.loads(line)['string_processor']['string_processor']
        template.close()

    def test_distance(self):
        print("Start distance test in StringProcessor")

        self.assertEqual(False, is_words_similar("юои", "юри"))
        self.assertEqual(True, is_words_similar("простая проверка", "поостая провекка"))

        print("Distance test in StringProcessor passed successfully!")

    def test_prepare_msg(self):
        print("Start prepare message test in StringProcessor")

        msg = prepare_msg(self.input_sp)
        self.assertEqual(self.sp, msg)

        msg = prepare_msg(self.input_su)
        self.assertEqual(self.su, msg)

        print("Prepare message test in StringProcessor passed successfully!")
