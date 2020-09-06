#!python
# coding: utf-8

"""
xkcd-wrapper BaseClient
"""

import json
from .comic import Comic
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
        self._response_int_values = {'num': 'id', 'year': 'date', 'month': 'date', 'day': 'date'}

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
        Parses the xkcd API response into a Comic object

        Parameters
        ----------
        response : str
            xkcd API json response as str

        Returns
        -------
        Comic

        Raises
        ------
        xkcd_wrapper.exceptions.BadResponseField
            If response contained a field that could not be converted to int after json decode
        """
        return json.loads(response, object_hook=self._json_to_comic)

    def _json_to_comic(self, response_dict):
        """
        json.loads() object_hook function

        Parameters
        ----------
        response_dict : dict
            xkcd API response as parsed by json.loads()

        Returns
        -------
        Comic

        Raises
        ------
        xkcd_wrapper.exceptions.BadResponseField
            If response_dict contained a field that could not be converted to int after json decode
        """
        # convert date values to int and ensure num is int
        for api_value, wrapper_value in self._response_int_values.items():
            try:
                response_dict[api_value] = int(response_dict[api_value])
            except ValueError as err:
                raise exceptions.BadResponseField(wrapper_value, api_value, err)

        comic_url = self._base_url.format(response_dict['num'], '')
        explanation_url = '{}{}'.format(self._explanation_wiki_url, response_dict['num'])

        return Comic(response_dict, comic_url=comic_url, explanation_url=explanation_url)
