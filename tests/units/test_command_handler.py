# -*- coding: utf-8 -*-

import json
import unittest

import pkg_resources

from core.handlers.command_handler import CommandProcessor


class TestCommandHandler(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Init tests...\n" + "=" * 50 + "\n")

        cls.cp = CommandProcessor()

        resource_path = '/'.join(('../snippets', 'input.json'))
        template = pkg_resources.resource_stream(__name__, resource_path)
        line = template.read().decode('utf-8')
        cls.input_hello = json.loads(line)['messages']['command_hello']
        cls.input_com = json.loads(line)['messages']['command_com']
        cls.input_tag = json.loads(line)['messages']['command_tag']
        cls.input_errors = json.loads(line)['messages']['command_errors']
        cls.input_roll = json.loads(line)['messages']['command_roll']
        template.close()

        resource_path = '/'.join(('../snippets', 'model.json'))
        template = pkg_resources.resource_stream(__name__, resource_path)
        line = template.read().decode('utf-8')
        cls.roll = json.loads(line)['com_handler']['command_roll']
        template.close()

    def helloTest(self):
        print("Start hello test in CommandHandler")

        self.assertEqual(self.cp.execute(self.input_hello), "")

        print("Hello test in CommandHandler passed successfully!")
