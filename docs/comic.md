# xkcd_wrapper.Comic
xkcd comic representation

A `Comic` represents a single xkcd comic. `xkcd_wrapper.Client` generates `Comic` objects

## Parameters
The `Comic` class can be instantiated with the following parameters:
```Python
Comic(xkcd_dict)
```

| Parameter | Type / Value | Default | Description|
|:---:|:---:|:---:|---|
| xkcd_dict | dict | | dictionary containing all the fields parsed by the `Client` |

## Attributes
Instances of the `Comic` class have the following attributes. All attributes can be `None` if the value was omitted
from the xkcd API response, for some reason

| Attribute | Type / Value | Description |
|:---:|:---:|---|
| id | int / None | xkcd comic id |
| date | datetime.date / None | date when comic was released |
| title | str / None | comic title |
| description | str / None | comic description |
| transcript | str / None | comic transcript |
| image | str / None | image url |
| link | str / None | comic url |
| explanation | str / None | url to explainxkcd wiki |

## Special Methods
* \_\_repr__
