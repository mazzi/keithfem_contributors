#!/usr/bin/env python

import os

import requests
from jinja2 import Environment, FileSystemLoader
from requests.exceptions import HTTPError

SHOWS_URL = "https://keithfem2.airtime.pro/api/shows"
IMAGES_URL = "https://keithfem2.airtime.pro/api/show-logo?id="
KEY_FILTERING = "genre"
VALUE_FILTERING = ["Contributor", "Original"]
SHOWS_TO_AVOID_IDS = []


def filter_show(
    shows,
):
    shows_filtered = dict()
    for show in shows:
        if show[KEY_FILTERING] in VALUE_FILTERING:
            if (
                show["name"] not in shows_filtered.keys()
                and show["id"] not in SHOWS_TO_AVOID_IDS
            ):
                shows_filtered[show["name"]] = {
                    "id": show["id"],
                    "name": show["name"],
                    "description": show["description"],
                    "image": IMAGES_URL + str(show["id"]),
                }
    return dict(sorted(shows_filtered.items(), key=lambda item: item[0]))


def main():
    try:
        response = requests.get(SHOWS_URL)
        response.raise_for_status()
    except HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")
    else:
        shows_to_render = filter_show(response.json())

        file_loader = FileSystemLoader(
            os.path.join(os.path.dirname(__file__), "templates")
        )
        env = Environment(loader=file_loader)
        template = env.get_template("contributors.html")

        output = template.render(shows=shows_to_render.values())

        print(output)


if __name__ == "__main__":
    main()
