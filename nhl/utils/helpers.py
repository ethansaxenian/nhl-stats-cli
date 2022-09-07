import json
from datetime import datetime
from typing import Optional

import requests
from requests import Response

from nhl.utils.constants import API_BASE_URL, QueryArgs, SeasonType, YEAR_FORMAT


def echo(message: str, disable_rich_output: bool = True):
    if not disable_rich_output:
        try:
            from rich import print as rich_print

            rich_print(message)
        except ModuleNotFoundError:
            print(message)
    else:
        print(message)


def fetch(path: str, query_args: Optional[QueryArgs] = None) -> Response:
    query_str = (
        ("?" + "&".join([f"{k}={v}" for k, v in query_args])) if query_args else ""
    )
    url = f"{API_BASE_URL}{path}{query_str}"
    return requests.get(url)


def print_response(
    response: Response,
    pretty: bool = False,
    sort_keys: bool = False,
    no_colors: bool = False,
) -> None:
    response_json = json.dumps(
        response.json(), sort_keys=sort_keys, indent=2 if pretty else None
    )
    echo(response_json, no_colors)


def season_to_str(season: SeasonType) -> str:
    return season[0].strftime(YEAR_FORMAT) + season[1].strftime(YEAR_FORMAT)


def datetime_to_str(time: Optional[datetime], format_str: str) -> str:
    try:
        return time.strftime(format_str)
    except AttributeError:
        return ""
