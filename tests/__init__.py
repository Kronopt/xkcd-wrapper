#!python
# coding: utf-8

import datetime
import json


base_url = 'https://xkcd.com/'
latest_comic_url = 'https://xkcd.com/info.0.json'
comic_id_url = 'https://xkcd.com/{}/info.0.json'
explanation_wiki_url = 'https://www.explainxkcd.com/wiki/index.php/'
raw_comic_image = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x02\x00\x00\x00\x90wS\xde\x00\x00\x00\x01sRGB\x00\xae\xce\x1c\xe9\x00\x00\x00\x04gAMA\x00\x00\xb1\x8f\x0b\xfca\x05\x00\x00\x00\tpHYs\x00\x00\x16%\x00\x00\x16%\x01IR$\xf0\x00\x00\x00\x0cIDAT\x18Wc\xf8\xff\xff?\x00\x05\xfe\x02\xfe\xa75\x81\x84\x00\x00\x00\x00IEND\xaeB`\x82'

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


def check_comic(test_case, comic, example, raw_image=True):
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
    raw_image : bool
        if Comic was generated with a comic raw image or not
    """
    date = datetime.date(int(example['year']),
                         int(example['month']),
                         int(example['day']))

    test_case.assertEqual(comic.id, example['num'])
    test_case.assertEqual(comic.date, date)
    test_case.assertEqual(comic.title, example['safe_title'])
    test_case.assertEqual(comic.description, example['alt'])
    test_case.assertEqual(comic.transcript, example['transcript'])

    if raw_image:
        test_case.assertEqual(comic.image, raw_comic_image)
        test_case.assertEqual(comic.image_extension, 'png')
    else:
        test_case.assertIsNone(comic.image)
        test_case.assertIsNone(comic.image_extension)

    test_case.assertEqual(comic.image_url, example['img'])
    test_case.assertEqual(comic.comic_url, '{}{}'.format(base_url, example['num']))
    test_case.assertEqual(comic.explanation_url,
                          '{}{}'.format(explanation_wiki_url, example['num']))
