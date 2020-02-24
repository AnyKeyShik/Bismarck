# -*- coding: utf-8 -*-

import json
import re
import unittest

import pkg_resources

from core.command_processor import CommandProcessor


class TestCommandProcessor(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Init tests...\n" + "=" * 50 + "\n")

        resource_path = '/'.join(('../snippets', 'input.json'))
        template = pkg_resources.resource_stream(__name__, resource_path)
        line = template.read().decode('utf-8')
        cls.input_strings = json.loads(line)['messages']['command_processor']
        template.close()

        resource_path = '/'.join(('../snippets', 'model.json'))
        template = pkg_resources.resource_stream(__name__, resource_path)
        line = template.read().decode('utf-8')
        cls.noChoices = json.loads(line)['command_processor']['noChoices']
        template.close()

        cls.sp = CommandProcessor()
        cls.sp.__init__()

    def testOnlyOr(self):
        print("Start only or test in CommandProcessor")

        out = self.sp.execute("roll", self.input_strings[0])
        self.assertEqual(self.noChoices, out)

        print("Only or test in CommandProcessor passed successfully!")

    def testTwoChoicesTwoOr(self):
        print("Start two choices two or test in CommandProcessor")

        regexp = re.compile(u'с[ао]с')
        out = self.sp.execute("roll", self.input_strings[1])
        self.assertIsNone(re.match(regexp, out))

        print("Two choices two or test in CommandProcessor passed successfully!")

    def testOneOr(self):
        print("Start one or test in CommandProcessor")

        out = self.sp.execute("roll", self.input_strings[2])
        self.assertEqual(self.noChoices, out)

        print("One or test in CommandProcessor passed successfully!")

    def testNormalCase(self):
        print("Start normal case test in CommandProcessor")

        regexp = re.compile(u'с[ао]с')
        out = self.sp.execute("roll", self.input_strings[1])
        self.assertIsNone(re.match(regexp, out))

        print("Normal case test in CommandProcessor passed successfully!")
