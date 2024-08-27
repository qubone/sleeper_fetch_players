import requests
import os
from datetime import datetime, timezone

# Make the API request
url = "https://api.sleeper.app/v1/players/nfl"
response = requests.get(url)

# Check for a successful request
if response.status_code == 200:
    # Create the data directory if it doesn't exist
    os.makedirs("data", exist_ok=True)

    # Save the response content as a JSON file with a timestamp
    filename = f"data/sleeper_data_{datetime.now(timezone.utc).strftime('%Y%m%d')}.json"
    with open(filename, "wb") as file:
        file.write(response.content)
else:
    print(f"Failed to fetch data: {response.status_code}")
