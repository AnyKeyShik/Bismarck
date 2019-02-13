# -*- coding: utf-8 -*-

import json
import unittest
from unittest import mock

import pkg_resources

from utils.pictures.konachan_grabber import KonachanGrabber as KonaGrabber


def mocked_requests_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, flag_str, status_code):

            if flag_str is not None:
                resource_path = '/'.join(('../snippets', 'response.json'))
                template = pkg_resources.resource_stream(__name__, resource_path)
                line = template.read().decode('utf-8')
                self.json_data = [json.loads(line)['pictures'][0]]
                template.close()
            else:
                self.json_data = ""

            self.status_code = status_code

        def json(self):
            return self.json_data

    if args[0] == "http://konachan.com/post.json?tags=seifuku+rating:explicit+order:random&limit=1":
        return MockResponse('load_from_file', 200)

    return MockResponse(None, 404)


class TestPictureGrabber(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Init tests...\n" + "=" * 50 + "\n")

        resource_path = '/'.join(('../snippets', 'model.json'))
        template = pkg_resources.resource_stream(__name__, resource_path)
        line = template.read().decode('utf-8')
        cls.json_data = json.loads(line)['pictures'][0]
        template.close()

    @mock.patch('utils.pictures.konachan_grabber.requests.get', side_effect=mocked_requests_get)
    def test_successful(self, mock_get):
        print("Start successful test for get_picture in Konachan")

        kg = KonaGrabber()
        (url, pic_hash) = kg.get_picture("seifuku", "explicit")
        self.assertEqual((self.json_data['url'], self.json_data['hash']), (url, pic_hash))

        print("Successful test for get_picture in Konachan passed successfully!")

    @mock.patch('utils.pictures.konachan_grabber.requests.get', side_effect=mocked_requests_get)
    def test_not_found(self, mock_get):
        print("Start fail test for get_picture in Konachan")

        kg = KonaGrabber()
        (url, pic_hash) = kg.get_picture("qwerty", "qwerty")
        self.assertEqual(("", ""), (url, pic_hash))

        print("Fail test for get_picture in Konachan passed successfully!")
