# -*- coding: utf-8 -*-

import unittest
from unittest import mock
import json

from utils.grabbers import PictureGrabber
from exceptions import PictureNotFoundException


def mocked_requests_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            if json_data is not None:
                self.json_data = json.loads(json_data)
            else:
                self.json_data = ""
            self.status_code = status_code

        def json(self):
            return self.json_data

    if args[0] == 'http://konachan.com/post.json?tags=seifuku+rating:explicit+order:random&limit=1':
        return MockResponse('[{"id":138016,"tags":"amou_mikage bra breast_grab breasts game_cg kikurage nipples '
                            'panties pantyhose purple_eyes purple_hair purple_software seifuku sex shiawase_'
                            'kazokubu underwear","created_at":1339950343,"creator_id":20645,"author":"Wiresetc",'
                            '"change":466262,"source":"Shiawase Kazoku-bu CG","score":470,'
                            '"md5":"3f4b3aac84afefde14967839fc2b33a1","file_size":1066553,'
                            '"file_url":"https://konachan.com/image/3f4b3aac84afefde14967839fc2b33a1/'
                            'Konachan.com%20-%20138016%20amou_mikage%20bra%20breast_grab%20breasts%20game_cg%20'
                            'kikurage%20nipples%20panties%20pantyhose%20purple_eyes%20purple_hair%20'
                            'purple_software%20seifuku%20sex%20underwear.png","is_shown_in_index":true,'
                            '"preview_url":"https://konachan.com/data/preview/3f/4b/'
                            '3f4b3aac84afefde14967839fc2b33a1.jpg","preview_width":150,"preview_height":84,'
                            '"actual_preview_width":300,"actual_preview_height":169,"sample_url":'
                            '"https://konachan.com/jpeg/3f4b3aac84afefde14967839fc2b33a1/Konachan.com%20-%20'
                            '138016%20amou_mikage%20bra%20breast_grab%20breasts%20game_cg%20kikurage%20'
                            'nipples%20panties%20pantyhose%20purple_eyes%20purple_hair%20purple_software%20seifuku'
                            '%20sex%20underwear.jpg","sample_width":1280,"sample_height":720,"sample_file_size":0,'
                            '"jpeg_url":"https://konachan.com/jpeg/3f4b3aac84afefde14967839fc2b33a1/Konachan.com'
                            '%20-%20138016%20amou_mikage%20bra%20breast_grab%20breasts%20game_cg%20kikurage'
                            '%20nipples%20panties%20pantyhose%20purple_eyes%20purple_hair%20purple_software'
                            '%20seifuku%20sex%20underwear.jpg","jpeg_width":1280,"jpeg_height":720,'
                            '"jpeg_file_size":559707,"rating":"e","has_children":false,"parent_id":null,'
                            '"status":"active","width":1280,"height":720,"is_held":false,"frames_pending_string":'
                            '"","frames_pending":[],"frames_string":"","frames":[]}]', 200)

    if args[0] == 'https://yande.re/post.json?tags=pantsu+rating:explicit+order:random&limit=1':
        return MockResponse('[{"id":246724,"tags":"alia\'s_carnival mitha nanawind nipples no_bra open_shirt '
                            'ousaka_asuha pantsu panty_pull see_through seifuku thighhighs underboob undressing '
                            'wet wet_clothes","created_at":1362530161,"updated_at":1510318154,"creator_id":58373,'
                            '"approver_id":null,"author":"WtfCakes","change":2204774,"source":"","score":275,'
                            '"md5":"0bddcf135c86b95de0fedf008254a1f2","file_size":7399904,"file_ext":"png",'
                            '"file_url":"https://files.yande.re/image/0bddcf135c86b95de0fedf008254a1f2/yande.re'
                            '%20246724%20mitha%20nanawind%20nipples%20no_bra%20open_shirt%20ousaka_asuha%20pantsu'
                            '%20panty_pull%20see_through%20seifuku%20thighhighs%20underboob%20undressing%20wet'
                            '%20wet_clothes.png","is_shown_in_index":true,'
                            '"preview_url":"https://assets.yande.re/data/preview/0b/dd'
                            '/0bddcf135c86b95de0fedf008254a1f2.jpg","preview_width":150,"preview_height":106,'
                            '"actual_preview_width":300,"actual_preview_height":212,'
                            '"sample_url":"https://files.yande.re/sample/0bddcf135c86b95de0fedf008254a1f2/yande'
                            '.re%20246724%20sample%20mitha%20nanawind%20nipples%20no_bra%20open_shirt'
                            '%20ousaka_asuha%20pantsu%20panty_pull%20see_through%20seifuku%20thighhighs'
                            '%20underboob%20undressing%20wet%20wet_clothes.jpg","sample_width":1500,'
                            '"sample_height":1058,"sample_file_size":306877,'
                            '"jpeg_url":"https://files.yande.re/jpeg/0bddcf135c86b95de0fedf008254a1f2/yande.re'
                            '%20246724%20mitha%20nanawind%20nipples%20no_bra%20open_shirt%20ousaka_asuha%20pantsu'
                            '%20panty_pull%20see_through%20seifuku%20thighhighs%20underboob%20undressing%20wet'
                            '%20wet_clothes.jpg","jpeg_width":3967,"jpeg_height":2798,"jpeg_file_size":1430129,'
                            '"rating":"e","is_rating_locked":false,"has_children":true,"parent_id":null,'
                            '"status":"active","is_pending":false,"width":3967,"height":2798,"is_held":false,'
                            '"frames_pending_string":"","frames_pending":[],"frames_string":"","frames":[],'
                            '"is_note_locked":false,"last_noted_at":0,"last_commented_at":1362820737}]', 200)

    return MockResponse(None, 404)


class TestPictureGrabber(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Init tests...\n" + "=" * 50 + "\n")

    @mock.patch('utils.grabbers.konachan_grabber.requests.get', side_effect=mocked_requests_get)
    def test_kona_successful(self, mock_get):
        print("Start successful test for kona_picture get_picture()")

        pg = PictureGrabber()
        url = pg.get_picture("seifuku", "explicit")
        self.assertEqual(("https://konachan.com/image/3f4b3aac84afefde14967839fc2b33a1/Konachan.com%20-%20138016"
                          "%20amou_mikage%20bra%20breast_grab%20breasts%20game_cg%20kikurage%20nipples"
                          "%20panties%20pantyhose%20purple_eyes%20purple_hair%20purple_software%20seifuku"
                          "%20sex%20underwear.png", "3f4b3aac84afefde14967839fc2b33a1"), url)

        print("Test passed successfully!")

    @mock.patch('utils.grabbers.konachan_grabber.requests.get', side_effect=mocked_requests_get)
    def test_yande_successful(self, mock_get):
        print("Start successful test for yande_picture get_picture()")

        pg = PictureGrabber()
        url = pg.get_picture("pantsu", "explicit")
        self.assertEqual(("https://files.yande.re/image/0bddcf135c86b95de0fedf008254a1f2/yande.re%20246724%20mitha"
                          "%20nanawind%20nipples%20no_bra%20open_shirt%20ousaka_asuha%20pantsu%20panty_pull"
                          "%20see_through%20seifuku%20thighhighs%20underboob%20undressing%20wet%20wet_clothes.png",
                          "0bddcf135c86b95de0fedf008254a1f2"), url)

        print("Test passed successfully!")

    @mock.patch('utils.grabbers.konachan_grabber.requests.get', side_effect=mocked_requests_get)
    def test_not_found(self, mock_get):
        print("Start fail test for get_picture()")

        pg = PictureGrabber()
        with self.assertRaises(PictureNotFoundException):
            pg.get_picture("pantsu", "safe")
