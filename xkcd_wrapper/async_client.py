#!python
# coding: utf-8

"""
xkcd-wrapper Async Client
"""

import random
import aiohttp
from .base_client import BaseClient
from . import exceptions


class AsyncClient(BaseClient):
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

    async def get(self, comic_id, raw_comic_image=True):
        """
        Asynchronously retrieve an xkcd comic by id

        Parameters
        ----------
        comic_id : int
            xkcd comic id
        raw_comic_image : bool
            if raw comic image should be retrieved or not (implies an extra http request)

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
        if not isinstance(comic_id, int):
            raise TypeError('\'comic_id\' parameter must be an int.')

        comic = self._parse_response(await self._request_comic(comic_id))

        if raw_comic_image:
            raw_image = await self._request_raw_image(comic.image_url)
            comic.update_raw_image(raw_image)

        return comic

    async def get_latest(self, raw_comic_image=True):
        """
        Asynchronously retrieves the latest xkcd comic

        Parameters
        ----------
        raw_comic_image : bool
            if raw comic image should be retrieved or not (implies an extra http request)

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
        return await self.get(0, raw_comic_image=raw_comic_image)  # comic_id of 0 = latest comic

    # get_latest alias
    latest = get_latest

    async def get_random(self, raw_comic_image=True):
        """
        Asynchronously retrieves a random xkcd comic

        Parameters
        ----------
        raw_comic_image : bool
            if raw comic image should be retrieved or not (implies an extra http request)

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
        latest_comic_id = self._parse_response(await self._request_comic(0)).id
        random_id = random.randint(1, latest_comic_id)
        comic = self._parse_response(await self._request_comic(random_id))

        if raw_comic_image:
            raw_image = await self._request_raw_image(comic.image_url)
            comic.update_raw_image(raw_image)

        return comic

    # get_random alias
    random = get_random

    async def _request_comic(self, comic_id):
        """
        Handles asynchronous http requests with the xkcd API
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

    @staticmethod
    async def _request_raw_image(raw_image_url):
        """
        Handles xkcd comic raw image asynchronous requests

        Parameters
        ----------
        raw_image_url : str
            raw image url

        Returns
        -------
        bytes
            raw comic image
        """
        async with aiohttp.ClientSession() as session:
            async with session.get(raw_image_url) as raw_image_response:
                if raw_image_response.status != 200:
                    raise exceptions.HttpError(raw_image_response.status, raw_image_response.reason)
                raw_image_bytes = await raw_image_response.read()
        return raw_image_bytes

    def __repr__(self):
        return 'xkcd_wrapper.AsyncClient()'
