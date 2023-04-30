#!/usr/bin/env python3

class Lights:
    def toggle(light_id):
        import requests
        import json
        from auth import Auth

        auth = Auth.auth()

        response = requests.post(f"https://api.lifx.com/v1/lights/{light_id}/toggle", headers=auth)

    def breathe_effect(light_id, color):
        import requests
        import json
        from auth import Auth

        auth = Auth.auth()

        data = {
            "period": 2,
            "cycles": 10,
            "color": f"{color}",
        }

        response = requests.post(f"https://api.lifx.com/v1/lights/{light_id}/effects/breathe", data=data, headers=auth)

    def stop_effect(light_id):
        import requests
        import json
        from auth import Auth

        auth = Auth.auth()

        data = {
            "power_off": True
        }

        response = requests.post(f"https://api.lifx.com/v1/lights/{light_id}/effects/off", data=data, headers=auth)
