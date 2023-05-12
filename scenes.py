#!/usr/bin/env python3

class Scenes:

    def __init__(self):
        from auth import Auth

        self.auth = Auth()
        self.auth_headers = self.auth.auth()

    def get(self):
        """Print a list of all scenes on this account."""
        import json
        from requests import get
        from tabulate import tabulate

        response = get('https://api.lifx.com/v1/scenes', headers=self.auth_headers)
        response = json.loads(response.content)
        
        scenes = []
        
        for key in range(0, len(response)):
            scenes += [[response[key]["name"], response[key]["uuid"]]]
        
        scenes.sort()
        print(tabulate(scenes, headers=["Name", "ID"]))

    def activate(self, scene_id):
        """Activates the specified scene. Requires scene UUID."""
        from requests import put

        put(f'https://api.lifx.com/v1/scenes/scene_id:{scene_id}/activate', headers=self.auth_headers)
