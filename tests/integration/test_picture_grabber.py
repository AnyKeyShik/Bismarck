# -*- coding: utf-8 -*-

import unittest

from core import PictureNotFoundException
from core.utils.pictures import PictureGrabber
from core.utils.proxy import patch


class TestPictureGrabber(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Init tests...\n" + "=" * 50 + "\n")
        patch()  # Set proxy

    def test_kona_successful(self):
        print("Start successful test for get picture")

        pg = PictureGrabber()
        url = pg.get_picture("seifuku", "explicit", False)
        self.assertNotEqual('', url)

        print("Successful test for get picture successfully!")

    def test_not_found(self):
        print("Start fail test for get picture")

        pg = PictureGrabber()
        with self.assertRaises(PictureNotFoundException):
            pg.get_picture("qwerty", "qwerty", True)

        print("Fail test for get picture successfully!")
