#!python
# coding: utf-8

"""
xkcd-wrapper
A wrapper for the xkcd API

Usage:
>>> import xkcd_wrapper
>>> client = xkcd_wrapper.Client()
>>> specific_comic = client.get(100)        # Comic object with comic 100 data
>>> latest_comic = client.get_latest()      # Comic object containing data of the latest xkcd comic
>>> random_comic = client.get_random()      # Comic object of a random comic

Async Usage:
>>> import xkcd_wrapper, asyncio
>>> async_client = xkcd_wrapper.AsyncClient()
>>> async def async_call():
...     responses = await asyncio.gather(
...         async_client.get(100),          # Comic object with comic 100 data
...         async_client.get_latest(),      # Comic object containing data of the latest xkcd comic
...         async_client.get_random()       # Comic object of a random comic
...     )
>>> asyncio.run(async_call())
"""

__author__ = 'Pedro HC David, https://github.com/Kronopt'
__credits__ = ['Pedro HC David']
__license__ = 'GPLv3'
__version__ = '0.2.2a'


requests_installed = True
aiohttp_installed = True

try:
    from .client import Client
except ModuleNotFoundError:
    requests_installed = False

try:
    from .async_client import AsyncClient
except ModuleNotFoundError:
    aiohttp_installed = False

if not any([requests_installed, aiohttp_installed]):
    raise ModuleNotFoundError(
        'Neither \'requests\' nor \'aiohttp\' are installed. '
        'xkcd-wrapper needs at least one of those dependencies to work. '
        'Use the correct pip command to install the necessary dependencies '
        '(please refer to the xkcd-wrapper documentation).')

from .comic import Comic
from . import exceptions
