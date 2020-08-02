# Usage

`xkcd-wrapper` retrieves all the information about xkcd comics through the xkcd API.
To start retrieving xkcd comic data, start by importing `xkcd-wrapper`:

```python
import xkcd_wrapper
```

then instantiate the `Client`:

```python
client = xkcd_wrapper.Client() 
```

Then you can use one of the available methods to retrieve xkcd comics:

* `get(<id>)` -> retieves comic by id
* `get_latest()` -> retrieves the latest comic (can also be called as just `latest()`)
* `get_random()` -> retrieves a random comic (can also be called as just `random()`)

All methods return a `Comic` object which contains the structured xkcd comic data.

```python
comic = client.get_latest()
```

The data is accessible as properties. You can access them like so:
```python
comic.id            # comic number
comic.date          # date of release
comic.title         # title
comic.description   # description
comic.transcript    # dialog and scene transcript
comic.image         # image url
comic.link          # comic webpage url
comic.explanation   # xkcd explanation wiki url
```

### Async implementation

The `AsyncClient`can be used in much the same way as `Client`. After importing `xkcd_wrapper`, instantiate the `AsyncClient`:
```python
async_client = xkcd_wrapper.AsyncClient() 
```

Then the same methods are available as for `Client`, but they are all async:

* `get(<id>)` -> retieves comic by id
* `get_latest()` -> retrieves the latest comic (can also be called as just `latest()`)
* `get_random()` -> retrieves a random comic (can also be called as just `random()`)

All methods also return a `Comic` object.

```python
import asyncio
loop = asyncio.get_event_loop()
comic = loop.run_until_complete(async_client.get_random())
```
