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

response = requests.get('https://api.lifx.com/v1/lights/all', headers=headers)
response = json.loads(response.content)

devices = []

for key in range(0, len(response)):
    devices += [[response[key]["label"], response[key]["id"]]]

print(tabulate(devices, headers=["Name", "ID"]))
