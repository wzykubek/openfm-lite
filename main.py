#!/usr/bin/python3
from flask import Flask, url_for, render_template
import requests
import json

app = Flask(__name__)

response = json.loads(
    requests.get("https://open.fm/radio/api/v2/ofm/stations_slug.json").text
)

channels_names = {}

for channel in response["channels"]:
    channels_names[channel["id"]] = channel["name"]


@app.route("/")
def hello_world():
    return render_template(
        "index.html", channels=response["channels"], title="Open FM Lite"
    )


@app.route("/radio/<id>")
def radio(id):
    return render_template("radio.html", id=id, title=(channels_names.get(id)))


if __name__ == "__main__":
    app.run(debug=True)
