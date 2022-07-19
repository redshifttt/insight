# Insight Library

Python library for the Mars Insight Raw Images API.

Made with the intention of archiving all of the images from the Mars Insight
Lander project since, from the time of writing, it is close to being closed
down.

Also never made a library before so should be an experience.

### Requirements

* python-requests

* Python 3.10+ (not sure if any older versions work)

### Documentation

**Note:** does not yet support switching pages.

#### Defaults

```
results_per_page: int = 100
page: int = 0
start_sol: int = 1
end_sol: int = 5
camera: str = "idc"
image_directory: str = "images"
```

#### `set_results_per_page([results])`

Values:

* `results`: optional. Defaults to 100 results per page.

#### `set_sol_range([start, end])`

Values:

* `start`: optional. Defaults to 1.
* `end`: optional. Defaults to 5.

#### `set_camera([camera])`

Values:

* `camera`: optional. Defaults to `"icc"`.

#### `set_save_directory([directory])`

Values:

* `directory`: optional. Defaults to `"images"`. No need for a trailing slash
  as it is covered by the library.

