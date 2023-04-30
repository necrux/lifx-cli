#!/usr/bin/env python3

class Scenes:
    def get():
        import requests
        import json
        from tabulate import tabulate
        from auth import Auth
        
        auth = Auth.auth()

        response = requests.get('https://api.lifx.com/v1/scenes', headers=auth)
        response = json.loads(response.content)
        
        scenes = []
        
        for key in range(0, len(response)):
            scenes += [[response[key]["name"], response[key]["uuid"]]]
        
        scenes.sort()
        print(tabulate(scenes, headers=["Name", "ID"]))

    def activate(scene_id):
        import requests
        from auth import Auth

        auth = Auth.auth()

        response = requests.put(f'https://api.lifx.com/v1/scenes/scene_id:{scene_id}/activate', headers=auth)
