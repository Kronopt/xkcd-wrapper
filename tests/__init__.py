#!python
# coding: utf-8

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
