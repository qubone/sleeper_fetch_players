"""Script to fetch the latest database using the Sleeper API.
"""

import json
from pathlib import Path
from typing import Any, Optional

import requests
import click


def fetch_players(sport: str) -> Optional[Any]:
    """Fetches data from Sleeper API using HTTP GET.

    Args:
        sport (str): Sport to fetch data for

    Returns:
        Optional[Any]: Response data in JSON format or None
    """
    url = f"https://api.sleeper.app/v1/players/{sport}"
    try:
        response = requests.get(url, timeout=60)
        response.raise_for_status()

        if "application/json" in response.headers.get("Content-Type", ""):
            return response.json()
        print("Error: Unexpected content type. Expected JSON.")
        return None

    except requests.exceptions.ConnectionError as conn_err:
        print(f"Connection error occurred: {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        print(f"Timeout error occurred: {timeout_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
    except ValueError as json_err:
        print(f"JSON decoding error occurred: {json_err}")
    return None

@click.command()
@click.option("--sport", default="nfl", help="Sport to fetch data for")
def main(sport: str):
    """Main function to fetch data and save it to a file."""
    output_dir = Path(sport)
    output_dir.mkdir(exist_ok=True)
    file_path = output_dir / "sleeper_data_latest.json"
    response_data = fetch_players(sport)
    file_path.write_text(json.dumps(response_data, indent=4))

if __name__ == "__main__":
    main()