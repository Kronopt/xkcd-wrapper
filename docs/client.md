# xkcd_wrapper.Client
xkcd API client

The `Client` communicates with the xkcd API, parses its response and generates `Comic` objects

## Parameters
The `Client` class is instantiated without parameters

## Methods
Instances of the `Client` class have the following methods

### base_url
Returns the xkcd API base url
```Python
Client.base_url()
```

Returns: **str**

### latest_comic_url
Returns the xkcd API url for the latest comic
```Python
Client.latest_comic_url()
```

Returns: **str**

### comic_id_url
Returns the xkcd API url for a specific comic id
```Python
Client.comic_id_url(comic_id)
```

| Parameter | Type / Value | Default | Description |
|:---:|:---:|:---:|---|
| comic_id | int |  | xkcd comic id |

Returns: **str**

### get
Retrieves an xkcd comic by id
```Python
Client.get(comic_id)
```

| Parameter | Type / Value | Default | Description |
|:---:|:---:|:---:|---|
| comic_id | int |  | xkcd comic id |

Returns: **xkcd_wrapper.Comic**

Raises:
- **TypeError**: If `comic_id` is not an `int`
- **requests.HTTPError**, **requests.Timeout**: If an http error or a timeout occurs
- **xkcd_wrapper.exceptions.BadResponseField**: If response contained a field that could not be converted to `int` (after json decode)
- **xkcd_wrapper.exceptions.HttpError**: If an http code different from 200 is returned

### get_latest
Retrieves the latest xkcd comic
```Python
Client.get_latest()
Client.latest()
```

Returns: **xkcd_wrapper.Comic**

Raises:
- **requests.HTTPError**, **requests.Timeout**: If an http error or a timeout occurs
- **xkcd_wrapper.exceptions.BadResponseField**: If response contained a field that could not be converted to `int` (after json decode)
- **xkcd_wrapper.exceptions.HttpError**: If an http code different from 200 is returned

### get_random
Retrieves a random xkcd comic

Contacts the xkcd API twice: once to know how many comics there are and another to fetch a random comic
```Python
Client.get_random()
Client.random()
```

Returns: **xkcd_wrapper.Comic**

Raises:
- **requests.HTTPError**, **requests.Timeout**: If an http error or a timeout occurs
- **xkcd_wrapper.exceptions.BadResponseField**: If response contained a field that could not be converted to `int` (after json decode)
- **xkcd_wrapper.exceptions.HttpError**: If an http code different from 200 is returned

## Special Methods
* \_\_repr__
