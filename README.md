# Sleeper Fetch Players Updater

Using GitHub Actions to periodically perform HTTP GET to fetch players using Sleeper API.

The data is stored in JSON format in data directory.

Currently only direct requests to the JSON data base file is supported. Navigate to the JSON file in the data directory, use the raw file URL to GET data in your request.

Example usage:
curl https://raw.githubusercontent.com/qubone/sleeper_fetch_players/main/data/sleeper_data_20240828.json

Remember that the files are getting generated each day with a new time stamp so you need to use the correct URL.
