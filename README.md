# Insight Library

Python library for the Mars Insight Raw Images API.

Made with the intention of archiving all of the images from the Mars Insight
Lander project since, from the time of writing, it is close to being closed
down.

Also never made a library before so should be an experience.

## Requirements

* python-requests

* Python 3.10+ (not sure if any older versions work)

## Documentation

**Note:** does not yet support switching pages.

### Defaults

### Example Program

```python
import insight

insight = insight.Insight()

insight.start_sol = 1 # Default values
insight.end_sol = 5 # Default values
insight.camera = "icc" # Default values

# Download images from the ICC camera from Sol 1 to 5
insight.download_images()
```

### Attributes

#### `insight.results_per_page`

* Default value: 100

* Type: int

#### `insight.page`

* Default value: 0

* Type: int

#### `insight.start_sol`

* Default value: 1

* Type: int

#### `insight.end_sol`

* Default value: 5

* Type: int

#### `insight.camera`

* Default value: "icc"

* Type: str

#### `insight.output_directory`

* Default value: "images"

* Type: str
