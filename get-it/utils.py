import json
import os
from flask import abort

def load_data(filename):
    filepath = os.path.join('static', 'data', filename)
    try:
        with open(filepath) as f:
            return json.load(f)
    except FileNotFoundError:
        abort(404, description="Resource not found")

def load_template(filename):
    filepath = os.path.join('static', 'template', filename)
    try:
        with open(filepath) as f:
            return f.read()
    except FileNotFoundError:
        abort(404, description="Resource not found")

def save_data(nome, data):
    filepaths = f"static/data/{nome}"
    try:
        with open(filepaths, 'w') as file:
            json.dump(data, file)
    except FileNotFoundError:
        abort(404, description="Resource not found")