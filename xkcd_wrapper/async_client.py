#!python
# coding: utf-8

"""
xkcd-wrapper Async Client
"""

import random
import aiohttp
from .client import Client
from .comic import Comic
from . import exceptions


class AsyncClient(Client):
    """
    AsyncClient asynchronously communicates with the xkcd API, parses its response and generates
    Comic objects

    Methods
    -------
    base_url() : str
        base url for xkcd API
    latest_comic_url() : str
        url for latest xkcd comic
    comic_id_url(comic_id) : str
        url for xkcd comic with id = comic_id
    async get(comic_id) : Comic
        retrieves the xkcd comic with id = comic_id
    async get_latest() : Comic
        retrieves the latest xkcd comic
    async get_random() : Comic
        retrieves a random xkcd comic

    Raises
    ------
    TypeError
        When calling get(comic_id), if comic_id is not an int
    aiohttp.ClientResponseError, aiohttp.ClientConnectionError
        When calling get(id), get_latest() and get_random() if an http error, timeout, etc, occurs
    """

    async def get(self, comic_id):
        """
        Asynchronously retrieve an xkcd comic by id

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
        aiohttp.ClientResponseError, aiohttp.ClientConnectionError
            If an http error, timeout, etc, occurs
        xkcd_wrapper.exceptions.BadResponseField
            If response contained a field that could not be converted to int (after json decode)
        xkcd_wrapper.exceptions.HttpError
            If an http code different from 200 is returned
        """
        if isinstance(comic_id, int):
            parsed_response = self._parse_response(await self._request_comic(comic_id))
        else:
            raise TypeError('\'comic_id\' parameter must be an int.')

        return Comic(parsed_response)

    async def get_latest(self):
        """
        Asynchronously retrieves the latest xkcd comic

        Returns
        -------
        Comic
            xkcd comic

        Raises
        ------
        aiohttp.ClientResponseError, aiohttp.ClientConnectionError
            If an http error, timeout, etc, occurs
        xkcd_wrapper.exceptions.BadResponseField
            If response contained a field that could not be converted to int (after json decode)
        xkcd_wrapper.exceptions.HttpError
            If an http code different from 200 is returned
        """
        return await self.get(0)  # comic_id of 0 requests latest comic

    async def get_random(self):
        """
        Asynchronously retrieves a random xkcd comic

        Returns
        -------
        Comic
            xkcd comic

        Raises
        ------
        aiohttp.ClientResponseError, aiohttp.ClientConnectionError
            If an http error, timeout, etc, occurs
        xkcd_wrapper.exceptions.BadResponseField
            If response contained a field that could not be converted to int (after json decode)
        xkcd_wrapper.exceptions.HttpError
            If an http code different from 200 is returned
        """
        # this calls _request_comic twice (using 2 different sessions)
        # could work around this by passing a session to the _request_comic method, but will leave
        # this like it is as to not alter _request_comic method signature
        latest_comic_id = self._parse_response(await self._request_comic(0))['id']
        random_id = random.randint(1, latest_comic_id)
        parsed_response = self._parse_response(await self._request_comic(random_id))
        return Comic(parsed_response)

    async def _request_comic(self, comic_id):
        """
        Handles asynchronous http requests
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
        aiohttp.ClientResponseError, aiohttp.ClientConnectionError
            If an http error, timeout, etc, occurs
        xkcd_wrapper.exceptions.HttpError
            If an http code different from 200 is returned
        """
        if comic_id <= 0:
            comic_url = self.latest_comic_url()
        else:
            comic_url = self.comic_id_url(comic_id)

        async with aiohttp.ClientSession() as session:
            async with session.get(comic_url) as xkcd_response:
                if xkcd_response.status != 200:
                    raise exceptions.HttpError(xkcd_response.status, xkcd_response.reason)
                xkcd_response_json = await xkcd_response.text()

        return xkcd_response_json

    def __repr__(self):
        return 'xkcd_wrapper.AsyncClient()'
