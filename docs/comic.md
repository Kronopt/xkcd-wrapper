# xkcd_wrapper.Comic
xkcd comic representation

A `Comic` represents a single xkcd comic. `xkcd_wrapper.Client` and `xkcd_wrapper.AsyncClient` generate `Comic` objects

## Parameters
The `Comic` class can be instantiated with the following parameters:
```Python
Comic(xkcd_dict, raw_image=None, comic_url=None, explanation_url=None)
```

| Parameter | Type / Value | Default | Description|
|:---:|:---:|:---:|---|
| xkcd_dict | dict | | dictionary containing the xkcd API response json |
| raw_image | bytes / None | None | raw comic image |
| comic_url | str / None | None | xkcd comic url |
| explanation_url | str / None | None | explainxkcd wiki url |

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
| image | bytes / None | raw comic image |
| image_extension | str / None | comic image extension (ex: .png, .jpeg) |
| image_url | str / None | comic image url |
| comic_url | str / None | comic url |
| explanation | str / None | explainxkcd wiki url |

## Special Methods
* \_\_repr__
