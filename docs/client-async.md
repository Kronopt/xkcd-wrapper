# xkcd_wrapper.AsyncClient
xkcd API async client

The `AsyncClient` communicates asynchronously with the xkcd API, parses its response and generates `Comic` objects

## Parameters
The `AsyncClient` class is instantiated without parameters

## Methods
Instances of the `AsyncClient` class have the following methods:

### base_url
```Python
AsyncClient.base_url()
```
xkcd API base url

Returns: **str**

### latest_comic_url
```Python
AsyncClient.latest_comic_url()
```
xkcd API url for the latest comic

Returns: **str**

### comic_id_url
```Python
AsyncClient.comic_id_url(comic_id)
```
xkcd API url for a specific comic id

| Parameter | Type / Value | Default | Description |
|:---:|:---:|:---:|---|
| comic_id | int |  | xkcd comic id |

Returns: **str**

### async get
```Python
AsyncClient.get(comic_id)
```
Retrieves an xkcd comic by id

| Parameter | Type / Value | Default | Description |
|:---:|:---:|:---:|---|
| comic_id | int |  | xkcd comic id |

Returns: **xkcd_wrapper.Comic**

Raises:
- **TypeError**: If `comic_id` is not an `int`
- **aiohttp.ClientResponseError**, **aiohttp.ClientConnectionError**: If an http error, timeout, etc, occurs
- **xkcd_wrapper.exceptions.BadResponseField**: If response contained a field that could not be converted to `int` (after json decode)
- **xkcd_wrapper.exceptions.HttpError**: If an http code different from 200 is returned

### async get_latest
```Python
AsyncClient.get_latest()
AsyncClient.latest()
```
Retrieves the latest xkcd comic

Returns: **xkcd_wrapper.Comic**

Raises:
- **aiohttp.ClientResponseError**, **aiohttp.ClientConnectionError** If an http error, timeout, etc, occurs
- **xkcd_wrapper.exceptions.BadResponseField**: If response contained a field that could not be converted to `int` (after json decode)
- **xkcd_wrapper.exceptions.HttpError**: If an http code different from 200 is returned

### async get_random
```Python
AsyncClient.get_random()
AsyncClient.random()
```
Retrieves a random xkcd comic.
Contacts the xkcd API twice: once to know how many comics there are and another to fetch a random comic

Returns: **xkcd_wrapper.Comic**

Raises:
- **aiohttp.ClientResponseError**, **aiohttp.ClientConnectionError**: If an http error, timeout, etc, occurs
- **xkcd_wrapper.exceptions.BadResponseField**: If response contained a field that could not be converted to `int` (after json decode)
- **xkcd_wrapper.exceptions.HttpError**: If an http code different from 200 is returned

## Special Methods
* \_\_repr__
