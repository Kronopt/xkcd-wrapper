# xkcd-wrapper
[![python versions](https://img.shields.io/pypi/pyversions/xkcd-wrapper "supported python versions")](https://pypi.org/project/xkcd-wrapper)
[![build status](https://github.com/Kronopt/xkcd-wrapper/workflows/CI/badge.svg "build status")](https://github.com/Kronopt/xkcd-wrapper/actions?query=workflow%3ACI)
[![coverage](https://codecov.io/gh/Kronopt/xkcd-wrapper/branch/master/graph/badge.svg "code coverage")](https://codecov.io/gh/Kronopt/xkcd-wrapper)
[![docs status](https://readthedocs.org/projects/xkcd-wrapper/badge/?version=latest "documentation build status")](https://xkcd-wrapper.readthedocs.io/en/latest/)
[![license](https://img.shields.io/pypi/l/xkcd-wrapper "license")](https://github.com/Kronopt/xkcd-wrapper/blob/master/LICENSE)

[![pypi](https://img.shields.io/pypi/v/xkcd-wrapper "pypi package")](https://pypi.org/project/xkcd-wrapper)
[![pypi downloads](https://img.shields.io/pypi/dm/xkcd-wrapper "pypi downloads")](https://pypi.org/project/xkcd-wrapper)

A Python wrapper for the [xkcd webcomic](https://xkcd.com/) API.

Retrieves xkcd comic data and metadata as python objects.

Asynchronous ([async](https://docs.python.org/3/library/asyncio.html)) and synchronous implementations.

## Installation
At the command line, with `pip`,

synchronous implementation:
```sh
$ pip install xkcd-wrapper[sync]
```

async implementation:
```sh
$ pip install xkcd-wrapper[async]
```

## Usage

synchronous:
```python
>>> import xkcd_wrapper

>>> client = xkcd_wrapper.Client()
>>> specific_comic = client.get(100)        # Comic object with comic 100 data
>>> latest_comic = client.get_latest()      # Comic object containing data of the latest xkcd comic
>>> random_comic = client.get_random()      # Comic object of a random comic

>>> specific_comic
xkcd_wrapper.Comic(100)
>>> specific_comic.image
'https://imgs.xkcd.com/comics/family_circus.jpg'
```

async:
```python
>>> import xkcd_wrapper, asyncio
>>> async_client = xkcd_wrapper.AsyncClient()

>>> async def async_call():
...     responses = await asyncio.gather(
...         async_client.get(100),          # Comic object with comic 100 data
...         async_client.get_latest(),      # Comic object containing data of the latest xkcd comic
...         async_client.get_random()       # Comic object of a random comic
...     )
...     print(
...         responses[0],                   # async_client.get(100) output
...         responses[0].image,
...         sep='\n'
...     )

>>> asyncio.run(async_call())
xkcd_wrapper.Comic(100)
'https://imgs.xkcd.com/comics/family_circus.jpg'
```

## Documentation
Check the documentation for more details: https://xkcd-wrapper.readthedocs.io/en/latest
