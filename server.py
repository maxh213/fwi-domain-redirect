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

@app.route('/health', methods=['GET'])
def health():
    return jsonify(
        status="ok"
    )
    
if __name__ == '__main__':
    serve(app, port=8080)
