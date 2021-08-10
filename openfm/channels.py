import requests
import json

response = json.loads(
    requests.get("https://open.fm/radio/api/v2/ofm/stations_slug.json").text
)

channels = response["channels"]
channels_by_id = {}

for channel in channels:
    channels_by_id[channel["id"]] = channel["name"]
