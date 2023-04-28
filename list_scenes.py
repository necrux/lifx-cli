#!/usr/bin/env python3

import requests
import configparser
import json

from tabulate import tabulate

config = configparser.ConfigParser()
config.read('/home/wes/.keys')

token = config['lifx']['token']

headers = {
    "Authorization": "Bearer %s" % token,
}

response = requests.get('https://api.lifx.com/v1/scenes', headers=headers)
response = json.loads(response.content)

print(response)
scenes = []

for key in range(0, len(response)):
    scenes += [[response[key]["name"], response[key]["uuid"]]]

print(tabulate(scenes, headers=["Name", "ID"]))
