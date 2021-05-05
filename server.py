#! /usr/bin/env python3.6

import json
import os
import random
import uuid
from time import strftime, gmtime

from waitress import serve
from flask import Flask, jsonify, redirect

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_index():
    return redirect("https://fishwelfareinitiative.org/", code=302)

@app.route('/<path>', methods=['GET'])
def get_index_with_path(path):
    url = "https://fishwelfareinitiative.org/" + path
    return redirect(url, code=302)

if __name__ == '__main__':
    serve(app, port=8080)
