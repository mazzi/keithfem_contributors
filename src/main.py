#!/usr/bin/env python

import requests
import os
from requests.exceptions import HTTPError
from jinja2 import Environment, FileSystemLoader

SHOWS_URL="https://keithfem2.airtime.pro/api/shows"
IMAGES_URL="https://keithfem2.airtime.pro/api/show-logo?id="
KEY_FILTERING='genre'
VALUE_FILTERING='Original'

def filter_show(shows, ):
    shows_filtered = []
    for show in shows:
        if show[KEY_FILTERING] == VALUE_FILTERING:
            shows_filtered.append({
                'name': show['name'],
                'description' : show['description'],
                'image': IMAGES_URL + str(show['id'])
            })
    return shows_filtered

def main():
    try:
        response = requests.get(SHOWS_URL)
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        shows_to_render= filter_show(response.json())

        file_loader = FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates'))
        env = Environment(loader=file_loader)
        template = env.get_template('contributors.html')

        output = template.render(shows=shows_to_render)

        print(output)

if __name__ == "__main__":
    main()
