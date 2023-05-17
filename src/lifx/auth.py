#!/usr/bin/env python3
"""Configure and set authentication headers."""
import sys
import configparser
from os import path, environ, getenv


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
        api_key = input('What is your API token?: ')

        if path.exists(self.auth_file):
            config.read(self.auth_file)

        if not config.has_section(self.auth_file_section):
            config = configparser.RawConfigParser()
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

    def auth(self):
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
            'Authorization': f'Bearer {token}',
        }

        return headers
