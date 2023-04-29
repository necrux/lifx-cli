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
        
        print(tabulate(scenes, headers=["Name", "ID"]))
