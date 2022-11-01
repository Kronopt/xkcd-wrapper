#!python
# coding: utf-8

"""
Tests for xkcd_wrapper.Comic
"""

import datetime
import unittest
import xkcd_wrapper
from . import comic_id_url, explanation_wiki_url, raw_comic_image


test_dict = {
    "month": 2,
    "num": 10,
    "link": "",
    "year": 2020,
    "news": "",
    "safe_title": "test title",
    "transcript": "test transcript",
    "alt": "test description",
    "img": "http://test_image_url.png",
    "title": "test unused title",
    "day": 10,
}
test_dict_missing_values = {
    "unexpected_value": "",
}


class TestComic(unittest.TestCase):
    def test_comic_ok(self):
        c = xkcd_wrapper.Comic(
            test_dict, raw_comic_image, comic_id_url, explanation_wiki_url
        )
        self.assertIsInstance(c, xkcd_wrapper.Comic)

        # id
        self.assertEqual(c.id, test_dict.get("num"))

        # date
        self.assertEqual(c.date, datetime.date(2020, 2, 10))

        # title
        self.assertEqual(c.title, test_dict.get("safe_title"))

        # description
        self.assertEqual(c.description, test_dict.get("alt"))

        # transcript
        self.assertEqual(c.transcript, test_dict.get("transcript"))

        # image
        self.assertEqual(c.image, raw_comic_image)

        # image_extension
        self.assertEqual(c.image_extension, "png")

        # image_url
        self.assertEqual(c.image_url, test_dict.get("img"))

        # comic_url
        self.assertEqual(c.comic_url, comic_id_url)

        # explanation_url
        self.assertEqual(c.explanation_url, explanation_wiki_url)

        # __repr__
        self.assertEqual(str(c), "xkcd_wrapper.Comic(10)")

    def test_comic_missing_values(self):
        c = xkcd_wrapper.Comic(test_dict_missing_values)
        self.assertIsInstance(c, xkcd_wrapper.Comic)

        # id
        self.assertIsNone(c.id)

        # date
        self.assertIsNone(c.date)

        # title
        self.assertIsNone(c.title)

        # description
        self.assertIsNone(c.description)

        # transcript
        self.assertIsNone(c.transcript)

        # image
        self.assertIsNone(c.image)

        # image_extension
        self.assertIsNone(c.image_extension)

        # image_url
        self.assertIsNone(c.image_url)

        # comic_url
        self.assertIsNone(c.comic_url)

        # explanation_url
        self.assertIsNone(c.explanation_url)

        # __repr__
        self.assertEqual(str(c), "xkcd_wrapper.Comic(None)")

    def test_update_raw_image(self):
        c = xkcd_wrapper.Comic(test_dict)

        self.assertIsNone(c.image)
        self.assertIsNone(c.image_extension)

        c.update_raw_image(raw_comic_image)

        self.assertEqual(c.image, raw_comic_image)
        self.assertEqual(c.image_extension, "png")

    def test__determine_date(self):
        ok = {"year": 2020, "month": 2, "day": 10}
        missing_one = {"year": 2020, "month": 2}
        missing_all = {}

        self.assertEqual(
            xkcd_wrapper.Comic._determine_date(ok), datetime.date(2020, 2, 10)
        )
        self.assertIsNone(xkcd_wrapper.Comic._determine_date(missing_one))
        self.assertIsNone(xkcd_wrapper.Comic._determine_date(missing_all))

    def test__determine_image_extension(self):
        c = xkcd_wrapper.Comic(test_dict, raw_image=raw_comic_image)

        self.assertEqual(c._determine_image_extension(), "png")
