"""Script to fetch the latest database using the Sleeper API.
"""

import json
from pathlib import Path
from typing import Any

import requests

URL = "https://api.sleeper.app/v1/players/nfl"


def fetch_players() -> Any | None:
    """Fetches data from Sleeper API using HTTP GET.
    Response is validated with error handling.

    Returns:
        Any | None: Response data in JSON format or None
    """
    try:
        response = requests.get(URL, timeout=60)
        response.raise_for_status()

        if "application/json" in response.headers.get("Content-Type", ""):
            return response.json()
        print("Error: Unexpected content type. Expected JSON.")
        return None

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Connection error occurred: {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        print(f"Timeout error occurred: {timeout_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
    except ValueError as json_err:
        print(f"JSON decoding error occurred: {json_err}")
    return None


output_dir = Path("data")
output_dir.mkdir(exist_ok=True)
file_name = output_dir / "sleeper_data_latest.json"
response_data = fetch_players()
file_name.write_text(json.dumps(response_data, indent=4))
