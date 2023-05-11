#!/usr/bin/env python3

class Lights:
    def toggle(self, light_id, group):
        """Toggles the power for the specified light. Requires the device ID."""
        import requests
        from auth import Auth

        auth = Auth()
        auth_headers = auth.auth()

        if group:
            light_id = f'group_id:{light_id}'

        requests.post(f"https://api.lifx.com/v1/lights/{light_id}/toggle", headers=auth_headers)

    def set_state(self, light_id, group, color, power, brightness, duration, infrared):
        """Changes the state for the specified light. Requires the device ID as well as optional changes."""
        import requests
        from auth import Auth

        auth = Auth()
        auth_headers = auth.auth()

        payload = {
            "power": f"{power}",
            "color": f"{color}",
            "brightness": f"{brightness}",
            "duration": f"{duration}",
            "infrared": f"{infrared}",
        }

        if group:
            light_id = f'group_id:{light_id}'

        requests.put(f"https://api.lifx.com/v1/lights/{light_id}/state", data=payload, headers=auth_headers)

    def breathe_effect(self, light_id, group, color):
        """Activates the breath effect on the specified light (period: 2; cycles: 10). Requires the device ID and
        color."""
        import requests
        from auth import Auth

        auth = Auth()
        auth_headers = auth.auth()

        data = {
            "period": 2,
            "cycles": 10,
            "color": f"{color}",
        }

        if group:
            light_id = f'group_id:{light_id}'

        requests.post(f"https://api.lifx.com/v1/lights/{light_id}/effects/breathe", data=data, headers=auth_headers)

    def stop_effect(self, light_id, group):
        """Stop all effects on the specified light. Requires Light ID."""
        import requests
        from auth import Auth

        auth = Auth()
        auth_headers = auth.auth()

        data = {
            "power_off": True
        }

        if group:
            light_id = f'group_id:{light_id}'

        requests.post(f"https://api.lifx.com/v1/lights/{light_id}/effects/off", data=data, headers=auth_headers)
