#!python
# coding: utf-8

"""
Tests for xkcd_wrapper.Client
"""

import datetime
import json
import random
import unittest
import requests_mock
import xkcd_wrapper
from nose2.tools.params import params as nose2_params


base_url = 'https://xkcd.com/'
latest_comic_url = 'https://xkcd.com/info.0.json'
comic_id_url = 'https://xkcd.com/{}/info.0.json'
explanation_wiki_url = 'https://www.explainxkcd.com/wiki/index.php/'
with open('tests/xkcd_api_example_response_628.json') as example_628, \
     open('tests/xkcd_api_example_response_138.json') as example_138:
    xkcd_api_example_628_raw = example_628.read()
    xkcd_api_example_138_raw = example_138.read()

# num is int
# day, month, year are str
xkcd_api_example_628_dict = json.loads(xkcd_api_example_628_raw)
xkcd_api_example_138_dict = json.loads(xkcd_api_example_138_raw)


class TestClient(unittest.TestCase):

    def test_client_init(self):
        with requests_mock.mock() as mock:
            mock.get(requests_mock.ANY)
            c = xkcd_wrapper.Client()
        self.assertFalse(mock.called)  # no request was performed during Client init
        self.assertIsInstance(c, xkcd_wrapper.Client)
        self.assertIsInstance(c._base_url, str)
        self.assertIsInstance(c._api, str)
        self.assertIsInstance(c._explanation_wiki_url, str)

    def test_base_url(self):
        c = xkcd_wrapper.Client()
        self.assertEqual(c.base_url(), base_url)

    def test_latest_comic_url(self):
        c = xkcd_wrapper.Client()
        self.assertEqual(c.latest_comic_url(), latest_comic_url)

    @nose2_params(-1, 0, 1, 999999)
    def test_comic_id_url(self, _id):
        c = xkcd_wrapper.Client()
        self.assertEqual(c.comic_id_url(_id), comic_id_url.format(_id))

    def test_get(self):
        c = xkcd_wrapper.Client()
        with requests_mock.mock() as mock:
            mock.get(comic_id_url.format(628), text=xkcd_api_example_628_raw)
            response = c.get(628)
            self.check_comic(response, xkcd_api_example_628_dict)
            with self.assertRaises(TypeError):
                c.get('')
            with self.assertRaises(TypeError):
                c.get([1, 2, 3])

    def test_get_latest(self):  # let's assume the example_628 json is the latest comic
        c = xkcd_wrapper.Client()
        with requests_mock.mock() as mock:
            mock.get(latest_comic_url, text=xkcd_api_example_628_raw)
            response = c.get_latest()
            self.check_comic(response, xkcd_api_example_628_dict)
            # alias
            response = c.latest()
            self.check_comic(response, xkcd_api_example_628_dict)

    def test_get_random(self):  # let's assume the example_628 json is the latest comic
        c = xkcd_wrapper.Client()
        with requests_mock.mock() as mock:
            mock.get(latest_comic_url, text=xkcd_api_example_628_raw)
            mock.get(comic_id_url.format(138), text=xkcd_api_example_138_raw)
            random.seed(1)  # with latest comic being 628, random value will be 138
            response = c.get_random()
            self.assertEqual(response.id, xkcd_api_example_138_dict['num'])  # is it the random comic?
            self.check_comic(response, xkcd_api_example_138_dict)
            # alias
            random.seed(1)
            response = c.random()
            self.assertEqual(response.id, xkcd_api_example_138_dict['num'])  # is it the random comic?
            self.check_comic(response, xkcd_api_example_138_dict)

    def check_comic(self, comic, example):
        """
        Assert comic has the required values

        Parameters
        ----------
        comic : xkcd_wrapper.Comic
            Comic
        example : dict
            parsed xkcd API example json
        """
        date = datetime.date(int(example['year']),
                             int(example['month']),
                             int(example['day']))

        self.assertEqual(comic.date, date)
        self.assertEqual(comic.id, example['num'])
        self.assertEqual(comic.title, example['safe_title'])
        self.assertEqual(comic.description, example['alt'])
        self.assertEqual(comic.transcript, example['transcript'])
        self.assertEqual(comic.image, example['img'])
        self.assertEqual(comic.link, '{}{}'.format(base_url, example['num']))
        self.assertEqual(comic.explanation, '{}{}'.format(explanation_wiki_url, example['num']))
