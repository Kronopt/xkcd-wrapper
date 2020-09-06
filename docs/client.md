# xkcd_wrapper.Client
xkcd API client

The `Client` communicates with the xkcd API, parses its response and generates `Comic` objects

## Parameters
The `Client` class is instantiated without parameters

## Methods
Instances of the `Client` class have the following methods:

### base_url
```Python
Client.base_url()
```
xkcd API base url

Returns: **str**

### latest_comic_url
```Python
Client.latest_comic_url()
```
xkcd API url for the latest comic

Returns: **str**

### comic_id_url
```Python
Client.comic_id_url(comic_id)
```
xkcd API url for a specific comic id

| Parameter | Type / Value | Default | Description |
|:---:|:---:|:---:|---|
| comic_id | int |  | xkcd comic id |

Returns: **str**

### get
```Python
Client.get(comic_id, raw_comic_image=True)
```
Retrieves an xkcd comic by id

| Parameter | Type / Value | Default | Description |
|:---:|:---:|:---:|---|
| comic_id | int |  | xkcd comic id |
| raw_comic_image | bool | True | Indicates if raw comic image should be retrieved or not (implies an extra http request) |

Returns: **xkcd_wrapper.Comic**

Raises:
- **TypeError**: If `comic_id` is not an `int`
- **requests.HTTPError**, **requests.Timeout**: If an http error or a timeout occurs
- **xkcd_wrapper.exceptions.BadResponseField**: If response contained a field that could not be converted to `int` (after json decode)
- **xkcd_wrapper.exceptions.HttpError**: If an http code different from 200 is returned

### get_latest
```Python
Client.get_latest(raw_comic_image=True)
Client.latest(raw_comic_image=True)
```
Retrieves the latest xkcd comic

| Parameter | Type / Value | Default | Description |
|:---:|:---:|:---:|---|
| raw_comic_image | bool | True | Indicates if raw comic image should be retrieved or not (implies an extra http request) |

Returns: **xkcd_wrapper.Comic**

Raises:
- **requests.HTTPError**, **requests.Timeout**: If an http error or a timeout occurs
- **xkcd_wrapper.exceptions.BadResponseField**: If response contained a field that could not be converted to `int` (after json decode)
- **xkcd_wrapper.exceptions.HttpError**: If an http code different from 200 is returned

### get_random
```Python
Client.get_random(raw_comic_image=True)
Client.random(raw_comic_image=True)
```
Retrieves a random xkcd comic.
Contacts the xkcd API twice: once to know how many comics there are and another to fetch a random comic

| Parameter | Type / Value | Default | Description |
|:---:|:---:|:---:|---|
| raw_comic_image | bool | True | Indicates if raw comic image should be retrieved or not (implies an extra http request) |

Returns: **xkcd_wrapper.Comic**

Raises:
- **requests.HTTPError**, **requests.Timeout**: If an http error or a timeout occurs
- **xkcd_wrapper.exceptions.BadResponseField**: If response contained a field that could not be converted to `int` (after json decode)
- **xkcd_wrapper.exceptions.HttpError**: If an http code different from 200 is returned

## Special Methods
* \_\_repr__
