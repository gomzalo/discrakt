from flask import Flask
from Discrakt.discrakt import connect_discord

app = Flask(__name__)

@app.route("/")
def index():
    connect_discord()
    return "Siuuuu"