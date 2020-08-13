#!python
# coding: utf-8

"""
xkcd-wrapper BaseClient
"""

import json
from . import exceptions


class BaseClient:
    """
    BaseClient contains the methods common to both Client and AsyncClient
    This class alone doesn't communicate with the xkcd API
    """

    def __init__(self):
        """
        BaseClient init
        """
        self._base_url = 'https://xkcd.com/{}{}'
        self._api = 'info.0.json'
        self._explanation_wiki_url = 'https://www.explainxkcd.com/wiki/index.php/'

    def base_url(self):
        """
        xkcd base API url

        Returns
        -------
        str
            xkcd base API url
        """
        return self._base_url.format('', '')

    def latest_comic_url(self):
        """
        xkcd API url for latest comic

        Returns
        -------
        str
            xkcd API url for latest comic
        """
        return self._base_url.format(self._api, '')

    def comic_id_url(self, comic_id):
        """
        xkcd API url for comic with id = comic_id

        Parameters
        ----------
        comic_id : int
            xkcd comic id

        Returns
        -------
        str
            xkcd API url for comic with id = comic_id
        """
        return self._base_url.format(str(comic_id) + '/', self._api)

    def _parse_response(self, response):
        """
        Parses xkcd API response

        Parameters
        ----------
        response : str
            xkcd API json response as str

        Returns
        -------
        dict
            relevant fields, extracted from xkcd API response, plus some extra ones

        Raises
        ------
        xkcd_wrapper.exceptions.BadResponseField
            If response contained a field that could not be converted to int (after json decode)
        """
        # relation between xkcd-wrapper fields and xkcd API fields
        fields_relationship = {
            'id': 'num',
            'day': 'day',
            'month': 'month',
            'year': 'year',
            'title': 'safe_title',
            'description': 'alt',
            'transcript': 'transcript',
            'image': 'img',
        }

        json_response = json.loads(response)

        # all values default to None to avoid errors if the xkcd API returns missing data
        parsed = dict()

        for wrapper_value, api_value in fields_relationship.items():
            # if int conversion raises ValueError, something came wrong from the API
            if wrapper_value in ('id', 'day', 'month', 'year'):  # int
                try:
                    parsed[wrapper_value] = int(
                        json_response[api_value]) if api_value in json_response else None
                except ValueError as err:
                    raise exceptions.BadResponseField(wrapper_value, api_value, err)

            # everything converts to str, so no error here
            else:  # str
                parsed[wrapper_value] = str(
                    json_response[api_value]) if api_value in json_response else None

        parsed['link'] = self._base_url.format(
            parsed['id'], '') if parsed['id'] is not None else None
        parsed['explanation'] = '{}{}'.format(self._explanation_wiki_url,
                                              parsed['id']) if parsed['id'] is not None else None

        return parsed
