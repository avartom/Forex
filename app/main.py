from base64 import b64decode
import os
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
