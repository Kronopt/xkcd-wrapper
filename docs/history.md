# History

### 1.0.1 (28-02-2021)
* Deprecate Python 3.5
* Support Python 3.9
* Update dependencies

### 1.0.0 (06-09-2020)
* Reworked xkcd API response json decoding
* Reworked `Comic`
* `Client` and `AsyncClient` can now retrieve comic images

### 0.2.2 (13-08-2020)
* Fixed failing to import `xkcd_wrapper` if either only `requests` or `aiohttp` were installed

### 0.2.1 (11-08-2020)
* Separate dependencies
    (you can now use the async implementation without having to install the sync dependencies and vice versa)

### 0.2.0 (08-08-2020)
* Async implementation (`AsyncClient`)

### 0.1.0 (23-04-2020)
* First release on PyPI
* `Client` and `Comic` classes
