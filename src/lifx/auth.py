#!/usr/bin/env python3
"""Configure and set authentication headers."""
import sys
import configparser
from os import path, environ, getenv
from requests import get

API = 'https://api.lifx.com/v1'


class Auth:
    """Configure and set authentication headers."""

    def __init__(self):

        self.auth_file = f'{path.expanduser("~")}/.keys'
        self.auth_file_section = 'lifx'
        self.auth_file_key = 'token'
        self.auth_env_var = 'LIFX'

    def configure(self):
        """Configure/update the ini file for API authentication."""
        config = configparser.RawConfigParser()
        while True:
            api_key = input('What is your API token?: ')
            environ[self.auth_env_var] = api_key
            if not self.validate_token():
                print("API Token invalid.")
                print("Token Setup Guide: https://api.developer.lifx.com/reference/authentication")
            else:
                break

        if path.exists(self.auth_file):
            config.read(self.auth_file)

        if not config.has_section(self.auth_file_section):
            config.add_section(self.auth_file_section)
            config.set(self.auth_file_section, self.auth_file_key, api_key)

            with open(self.auth_file, 'a+', encoding='UTF-8') as file:
                config.write(file)
        else:
            overwrite = input('You already have an API key saved in ~/.keys. '
                              'Do you want to overwrite this value? y/N ')
            overwrite = overwrite.lower()

            if overwrite == 'y':
                config.set(self.auth_file_section, self.auth_file_key, api_key)

                with open(self.auth_file, 'w', encoding='UTF-8') as file:
                    config.write(file)
        sys.exit(0)

    def validate_token(self) -> bool:
        """Validate a provided token by querying the color API."""
        url = f'{API}/color?string=red'
        response = get(url, headers=self.auth(), timeout=5)
        if response.status_code == 401:
            return False
        if response.status_code != 200:
            print("Received an unexpected response from LIFX. Please try again.")
            return False
        return True

    def auth(self) -> dict:
        """Returns the headers required to authenticate to the LIFX API."""
        try:
            if environ.get(self.auth_env_var):
                token = getenv(self.auth_env_var)
            else:
                config = configparser.ConfigParser()
                config.read(self.auth_file)

                token = config[self.auth_file_section][self.auth_file_key]
        except KeyError:
            print("Must configure an API token first.")
            self.configure()

        headers = {
            "Authorization": f"Bearer {token}",
        }
        return headers
