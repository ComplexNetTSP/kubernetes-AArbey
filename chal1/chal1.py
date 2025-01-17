import os
from flask import Flask, render_template, request
from datetime import datetime


app = Flask(__name__)

@app.route("/")
def hello_world():
    date = datetime.now()

    return render_template(
        'index.html',
        date_now=date.strftime("%d/%m/%y"),
        serveur=request.base_url,
    )
