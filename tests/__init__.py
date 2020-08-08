#!python
# coding: utf-8

import datetime
import json


base_url = 'https://xkcd.com/'
latest_comic_url = 'https://xkcd.com/info.0.json'
comic_id_url = 'https://xkcd.com/{}/info.0.json'
explanation_wiki_url = 'https://www.explainxkcd.com/wiki/index.php/'

with open('tests/xkcd_api_example_response_628.json') as example_628, \
     open('tests/xkcd_api_example_response_138.json') as example_138, \
     open('tests/xkcd_api_example_response_wrong_fields.json') as example_wrong:
    xkcd_api_example_628_raw = example_628.read()
    xkcd_api_example_138_raw = example_138.read()
    xkcd_api_example_wrong_raw = example_wrong.read()

# num is int
# day, month, year are str
xkcd_api_example_628_dict = json.loads(xkcd_api_example_628_raw)
xkcd_api_example_138_dict = json.loads(xkcd_api_example_138_raw)


def check_comic(test_case, comic, example):
    """
    Assert comic has the required values

    Parameters
    ----------
    test_case : unittest.TestCase
        TestCase
    comic : xkcd_wrapper.Comic
        Comic
    example : dict
        parsed xkcd API example json
    """
    date = datetime.date(int(example['year']),
                         int(example['month']),
                         int(example['day']))

    test_case.assertEqual(comic.date, date)
    test_case.assertEqual(comic.id, example['num'])
    test_case.assertEqual(comic.title, example['safe_title'])
    test_case.assertEqual(comic.description, example['alt'])
    test_case.assertEqual(comic.transcript, example['transcript'])
    test_case.assertEqual(comic.image, example['img'])
    test_case.assertEqual(comic.link, '{}{}'.format(base_url, example['num']))
    test_case.assertEqual(comic.explanation, '{}{}'.format(explanation_wiki_url, example['num']))
