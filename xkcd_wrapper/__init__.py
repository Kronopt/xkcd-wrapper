#!python
# coding: utf-8

"""
xkcd-wrapper
A wrapper for the xkcd API

Usage:
>>> import xkcd_wrapper
>>> client = xkcd_wrapper.Client()
>>> latest_comic = client.get_latest()  # Comic object containing the latest xkcd comic
>>> specific_comic = client.get(100)    # Comic with id 100
>>> random_comic = client.get_random()  # Random comic
"""

__author__ = 'Pedro HC David, https://github.com/Kronopt'
__credits__ = ['Pedro HC David']
__license__ = 'GPLv3'
__version__ = '0.1.0'


from .client import Client
from .async_client import AsyncClient
from .comic import Comic
from . import exceptions
