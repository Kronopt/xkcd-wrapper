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
    'id':           10,
    'title':        'test title',
    'description':  'test description',
    'transcript':   'test transcript',
    'image':        'http://test_image_url',
    'link':         'http://test_comic_url',
    'explanation':  'http://test_explanation_url',
    'day':          10,
    'month':        2,
    'year':         2020,
}
test_dict_none = {key: None for key in test_dict}   # same dict but all None values


class TestComic(unittest.TestCase):

    @nose2_params(test_dict, test_dict_none)
    def test_comic_init(self, xkcd_dict):
        c = xkcd_wrapper.Comic(xkcd_dict)
        self.assertIsInstance(c, xkcd_wrapper.Comic)
        self.assertIsInstance(c._comic, dict)

    @nose2_params(test_dict, test_dict_none)
    def test_id(self, xkcd_dict):
        c = xkcd_wrapper.Comic(xkcd_dict)
        self.assertEqual(c._comic['id'], xkcd_dict['id'])
        self.assertEqual(c.id, xkcd_dict['id'])
        if c.id is not None:
            self.assertIsInstance(c.id, int)

    @nose2_params(test_dict, test_dict_none)
    def test_title(self, xkcd_dict):
        c = xkcd_wrapper.Comic(xkcd_dict)
        self.assertEqual(c._comic['title'], xkcd_dict['title'])
        self.assertEqual(c.title, xkcd_dict['title'])
        if c.title is not None:
            self.assertIsInstance(c.title, str)

    @nose2_params(test_dict, test_dict_none)
    def test_description(self, xkcd_dict):
        c = xkcd_wrapper.Comic(xkcd_dict)
        self.assertEqual(c._comic['description'], xkcd_dict['description'])
        self.assertEqual(c.description, xkcd_dict['description'])
        if c.description is not None:
            self.assertIsInstance(c.description, str)

    @nose2_params(test_dict, test_dict_none)
    def test_transcript(self, xkcd_dict):
        c = xkcd_wrapper.Comic(xkcd_dict)
        self.assertEqual(c._comic['transcript'], xkcd_dict['transcript'])
        self.assertEqual(c.transcript, xkcd_dict['transcript'])
        if c.transcript is not None:
            self.assertIsInstance(c.transcript, str)

    @nose2_params(test_dict, test_dict_none)
    def test_image(self, xkcd_dict):
        c = xkcd_wrapper.Comic(xkcd_dict)
        self.assertEqual(c._comic['image'], xkcd_dict['image'])
        self.assertEqual(c.image, xkcd_dict['image'])
        if c.image is not None:
            self.assertIsInstance(c.image, str)

    @nose2_params(test_dict, test_dict_none)
    def test_link(self, xkcd_dict):
        c = xkcd_wrapper.Comic(xkcd_dict)
        self.assertEqual(c._comic['link'], xkcd_dict['link'])
        self.assertEqual(c.link, xkcd_dict['link'])
        if c.link is not None:
            self.assertIsInstance(c.link, str)

    @nose2_params(test_dict, test_dict_none)
    def test_explanation(self, xkcd_dict):
        c = xkcd_wrapper.Comic(xkcd_dict)
        self.assertEqual(c._comic['explanation'], xkcd_dict['explanation'])
        self.assertEqual(c.explanation, xkcd_dict['explanation'])
        if c.explanation is not None:
            self.assertIsInstance(c.explanation, str)

    @nose2_params(test_dict)
    def test_date(self, xkcd_dict):
        c = xkcd_wrapper.Comic(xkcd_dict)
        self.assertEqual(c.date, c._comic['date'])
        self.assertIsInstance(c.date, datetime.date)

        # day is None
        xkcd_dict['day'] = None
        c = xkcd_wrapper.Comic(xkcd_dict)
        self.assertEqual(c.date, c._comic['date'])
        self.assertIsNone(c.date)

        # month is None
        xkcd_dict['day'] = 10
        xkcd_dict['month'] = None
        c = xkcd_wrapper.Comic(xkcd_dict)
        self.assertEqual(c.date, c._comic['date'])
        self.assertIsNone(c.date)

        # year is None
        xkcd_dict['month'] = 2
        xkcd_dict['year'] = None
        c = xkcd_wrapper.Comic(xkcd_dict)
        self.assertEqual(c.date, c._comic['date'])
        self.assertIsNone(c.date)

        # all 3 are None
        xkcd_dict['day'] = None
        xkcd_dict['month'] = None
        c = xkcd_wrapper.Comic(xkcd_dict)
        self.assertEqual(c.date, c._comic['date'])
        self.assertIsNone(c.date)
