# The Unofficial LIFX CLI

This is a work in progress to create a feature-rich LIFX CLI.

**This project is not affiliated with or endorsed by LIFX.**

## Installation

```
pip install lifx-cli
```

## Authentication

Authentication is done using your token stored in `~/.keys`. This can be configured manually or by running `lifx --configure`.

**Example `~/.keys` *ini* file:**

```
[lifx]
token = FAKE_TOKEN
```

Alternatively, you can override this value by setting the `LIFX` environment variable:

```
export LIFX=FAKE_TOKEN
```

Refer to the [documentation](https://api.developer.lifx.com/reference/how-to-use-the-following-examples) in order to generate your own token.

## Targeting Lights

The LIFX CLI primary uses device/group/scene IDs to operate, however LIFX does provide multiple options for the light 'selectors'. While not yet officially available via the CLI, you can tap into these options by prefacing your light ID accordingly (if there are spaces in the name, simply enclose in `"`).

```
lifx lights --toggle all
lifx lights --toggle "label:Left Lamp"
lifx lights --toggle "group: Upstairs Lights"
lifx lights --toggle "location_id:1d6fe8ef0fde4c6d77b0012dc736662c"
lifx lights --toggle "location:Home"
```

### Finding the Proper ID

In order to get a listing of device and group IDs, simply run `--list` with the `lights` sub-command.

```
lifx lights --list
```

In order to get a listing of scene IDs, run the same command for `scenes`.

```
lifx scenes --list
```

### Setting colors

Colors can be set by name, e.g. `red`, `yellow`, but the CLI also supports all methods to set the color that the API supports.

In order to see a full list of supported methods run `lifx colors --list`. You can also validate a color's HSBK *(hue, saturation, brightness, and kelvin)* via `lifx colors --color red`.

