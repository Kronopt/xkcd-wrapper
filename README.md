# xkcd-wrapper
[![python versions](https://img.shields.io/pypi/pyversions/xkcd-wrapper "supported python versions")](https://pypi.org/project/xkcd-wrapper)
[![build status](https://github.com/Kronopt/xkcd-wrapper/workflows/CI/badge.svg "build status")](https://github.com/Kronopt/xkcd-wrapper/actions?query=workflow%3ACI)
[![coverage](https://codecov.io/gh/Kronopt/xkcd-wrapper/branch/master/graph/badge.svg "code coverage")](https://codecov.io/gh/Kronopt/xkcd-wrapper)
[![docs status](https://readthedocs.org/projects/xkcd-wrapper/badge/?version=latest "documentation build status")](https://xkcd-wrapper.readthedocs.io/en/latest/)
[![license](https://img.shields.io/pypi/l/xkcd-wrapper "license")](https://github.com/Kronopt/xkcd-wrapper/blob/master/LICENSE)

[![pypi](https://img.shields.io/pypi/v/xkcd-wrapper "pypi package")](https://pypi.org/project/xkcd-wrapper)
[![pypi downloads](https://img.shields.io/pypi/dm/xkcd-wrapper "pypi downloads")](https://pypi.org/project/xkcd-wrapper)

A Python wrapper for the [xkcd webcomic](https://xkcd.com/) API.

Retrieve xkcd comic data and metadata as python objects.

## Installation
At the command line, with `pip`:
```sh
$ pip install xkcd-wrapper
```

## Usage
```python
>>> import xkcd_wrapper
>>> client = xkcd_wrapper.Client()
>>> latest_comic = client.get_latest()      # Comic object containing data of the latest xkcd comic
>>> specific_comic = client.get(100)        # Comic object with comic 100 data
>>> random_comic = client.get_random()      # Comic object of a random comic

>>> specific_comic
xkcd_wrapper.Comic(100)
>>> specific_comic.image
'https://imgs.xkcd.com/comics/family_circus.jpg'
```

Check the documentation for more details: https://xkcd-wrapper.readthedocs.io/en/latest

#### Ideas for the Future
* retrieve comic .jpeg
* async client

