#!python
# coding: utf-8

"""
xkcd-wrapper Client
"""

import random
import requests
from .base_client import BaseClient
from .comic import Comic
from . import exceptions


class Client(BaseClient):
    """
    Client communicates with the xkcd API, parses its response and generates Comic objects

    Methods
    -------
    base_url() : str
        base url for xkcd API
    latest_comic_url() : str
        url for latest xkcd comic
    comic_id_url(comic_id) : str
        url for xkcd comic with id = comic_id
    get(comic_id) : Comic
        retrieves the xkcd comic with id = comic_id
    get_latest() : Comic
        retrieves the latest xkcd comic
    get_random() : Comic
        retrieves a random xkcd comic

    Raises
    ------
    TypeError
        When calling get(comic_id), if comic_id is not an int
    requests.HTTPError, requests.Timeout
        When calling get(id), get_latest() and random() if an http error or a timeout occurs
    """

    def get(self, comic_id):
        """
        Retrieve an xkcd comic by id

        Parameters
        ----------
        comic_id : int
            xkcd comic id

        Returns
        -------
        Comic
            xkcd comic

        Raises
        ------
        TypeError
            If comic_id is not an int
        requests.HTTPError, requests.Timeout
            If an http error or a timeout occurs
        xkcd_wrapper.exceptions.BadResponseField
            If response contained a field that could not be converted to int (after json decode)
        xkcd_wrapper.exceptions.HttpError
            If an http code different from 200 is returned
        """
        if not isinstance(comic_id, int):
            raise TypeError('\'comic_id\' parameter must be an int.')
        return self._parse_response(self._request_comic(comic_id))

    def get_latest(self):
        """
        Retrieves the latest xkcd comic

        Returns
        -------
        Comic
            xkcd comic

        Raises
        ------
        requests.HTTPError, requests.Timeout
            If an http error or a timeout occurs
        xkcd_wrapper.exceptions.BadResponseField
            If response contained a field that could not be converted to int (after json decode)
        xkcd_wrapper.exceptions.HttpError
            If an http code different from 200 is returned
        """
        return self.get(0)  # comic_id of 0 requests latest comic

    # get_latest alias
    latest = get_latest

    def get_random(self):
        """
        Retrieves a random xkcd comic

        Returns
        -------
        Comic
            xkcd comic

        Raises
        ------
        requests.HTTPError, requests.Timeout
            If an http error or a timeout occurs
        xkcd_wrapper.exceptions.BadResponseField
            If response contained a field that could not be converted to int (after json decode)
        xkcd_wrapper.exceptions.HttpError
            If an http code different from 200 is returned
        """
        # This method has to contact the xkcd API twice: first to get the latest comic id, and then
        # to get the actual randomized comic.
        # I could store the id of the latest comic and use it on subsequent get_random() calls, but
        # then I would have to handle that id being too old if the client stays up for a while...
        latest_comic_id = self._parse_response(self._request_comic(0)).id
        random_id = random.randint(1, latest_comic_id)
        return self._parse_response(self._request_comic(random_id))

    # get_random alias
    random = get_random

    def _request_comic(self, comic_id):
        """
        Handles http requests
        comic_id <= 0: requests latest comic
        comic_id >  0: requests comic with id = comic_id

        Parameters
        ----------
        comic_id : int
            xkcd comic id

        Returns
        -------
        str
            xkcd API json response as str

        Raises
        ------
        requests.HTTPError, requests.Timeout
            If an http error or a timeout occurs
        xkcd_wrapper.exceptions.HttpError
            If an http code different from 200 is returned
        """
        if comic_id <= 0:
            comic_url = self.latest_comic_url()
        else:
            comic_url = self.comic_id_url(comic_id)

        xkcd_response = requests.get(comic_url)
        if xkcd_response.status_code != 200:
            raise exceptions.HttpError(xkcd_response.status_code, xkcd_response.reason)
        return xkcd_response.text

    def __repr__(self):
        return 'xkcd_wrapper.Client()'
