#!python
# coding: utf-8

"""
Tests for xkcd_wrapper.Comic
"""

import datetime
import unittest
import xkcd_wrapper
from nose2.tools.params import params as nose2_params


test_dict = {
    'month':         2,
    'num':           10,
    'link':          '',
    'year':         2020,
    'news':         '',
    'safe_title':   'test title',
    'transcript':   'test transcript',
    'alt':          'test description',
    'img':          'http://test_image_url.png',
    'title':        'test unused title',
    'day':          10,
}
test_dict_missing_values = {
    'link': '',
    'year': 2020,
    'news': '',
    'title': 'test unused title',
    'day': 10,
}

raw_image = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x02\x00\x00\x00\x90wS\xde\x00\x00\x00\x01sRGB\x00\xae\xce\x1c\xe9\x00\x00\x00\x04gAMA\x00\x00\xb1\x8f\x0b\xfca\x05\x00\x00\x00\tpHYs\x00\x00\x16%\x00\x00\x16%\x01IR$\xf0\x00\x00\x00\x0cIDAT\x18Wc\xf8\xff\xff?\x00\x05\xfe\x02\xfe\xa75\x81\x84\x00\x00\x00\x00IEND\xaeB`\x82'
comic_url = 'http://test_comic_url'
explanation_url = 'http://test_explanation_url'


class TestComic(unittest.TestCase):

    @nose2_params(test_dict, test_dict_missing_values)
    def test_comic(self, xkcd_dict):
        c = xkcd_wrapper.Comic(xkcd_dict, raw_image, comic_url, explanation_url)
        self.assertIsInstance(c, xkcd_wrapper.Comic)

        # id
        self.assertEqual(c.id, xkcd_dict.get('num'))

        # date
        if all([xkcd_dict.get('year'), xkcd_dict.get('month'), xkcd_dict.get('day')]):
            self.assertEqual(c.date, datetime.date(2020, 2, 10))
        else:
            self.assertIsNone(c.date)

        # title
        self.assertEqual(c.title, xkcd_dict.get('safe_title'))

        # description
        self.assertEqual(c.description, xkcd_dict.get('alt'))

        # transcript
        self.assertEqual(c.transcript, xkcd_dict.get('transcript'))

        # image
        self.assertEqual(c.image, raw_image)

        # image_extension
        self.assertEqual(c.image_extension, 'png')

        # image_url
        self.assertEqual(c.image_url, xkcd_dict.get('img'))

        # comic_url
        self.assertEqual(c.comic_url, comic_url)

        # explanation_url
        self.assertEqual(c.explanation_url, explanation_url)

        if c.id:
            self.assertEqual(str(c), 'xkcd_wrapper.Comic(10)')
        else:
            self.assertEqual(str(c), 'xkcd_wrapper.Comic(None)')
