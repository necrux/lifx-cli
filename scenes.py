#!/usr/bin/env python3

class Scenes:
    def get(self):
        """Prints a list of all scenes on this account."""
        import requests
        import json
        from tabulate import tabulate
        from auth import Auth

        auth = Auth()
        auth_headers = auth.auth()

        response = requests.get('https://api.lifx.com/v1/scenes', headers=auth_headers)
        response = json.loads(response.content)
        
        scenes = []
        
        for key in range(0, len(response)):
            scenes += [[response[key]["name"], response[key]["uuid"]]]
        
        scenes.sort()
        print(tabulate(scenes, headers=["Name", "ID"]))

    def activate(self, scene_id):
        """Activates the specified scene. Requires scene UUID."""
        import requests
        from auth import Auth

        auth = Auth()
        auth_headers = auth.auth()

        requests.put(f'https://api.lifx.com/v1/scenes/scene_id:{scene_id}/activate', headers=auth_headers)
