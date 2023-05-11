# The Unofficial LIFX CLI
Playing around with the LifX API with the goal of creating a CLI.

## Authentication
Authentication is done using your token which is stored in `~/.keys`. This can be configured by running `lifx --configure`. 

**Example `~/.keys` *ini* file:**

```
[lifx]
token = FAKE_TOKEN
```

Alternatively, you can override this value by setting the `LIFX` environment variable:

```
export LIFX=FAKE_TOKEN
```

Refer to the [documentation](https://api.developer.lifx.com/reference/authentication) in order to generate your own token.

## Targeting Lights

The LIFX CLI primary uses device/group/scene IDs to operate, however LIFX does provide multiple options for the light 'selectors'. While not yet officially available via the CLI, you can tap into these options by prefacing your light ID with the correct prefix (if there are spaces in the name, simply enclose in `"`).

```
lifx --toggle --light all
lifx --toggle --light "label:Left Lamp"
lifx --toggle --light "group: Upstairs Lights"
lifx --toggle --light "location_id:1d6fe8ef0fde4c6d77b0012dc736662c"
lifx --toggle --light "location:Home"
```

Use the `--devices` options in order to get a list of devices with their device ID and corresponding group ID. Use the `--scenes` option to get a list of scenes and their corresponding IDs.