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