#!/usr/bin/env python3

class Lights:
    def toggle(light):
        import requests
        import json
        from auth import Auth

        auth = Auth.auth()

        response = requests.post(f"https://api.lifx.com/v1/lights/{light}/toggle", headers=auth)
