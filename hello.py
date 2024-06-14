from flask import Flask, jsonify
import subprocess

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'


@app.route('/packages')
def list_packages():
    result = subprocess.run(['pip', 'list'], capture_output=True, text=True)
    packages = result.stdout
    return f'<pre>{packages}</pre>'

