from flask import url_for, render_template
from . import app
from .channels import channels, channels_by_id


@app.route("/")
def home():
    return render_template(
        "index.j2", channels=channels, title="Open FM Lite"
    )


@app.route("/radio/<id>")
def radio(id):
    return render_template("radio.j2", id=id, title=(channels_by_id.get(id)))
