from flask import Flask, request, send_file, jsonify
import json

app = Flask(__name__)


@app.route('/')
def index():
    return 'hello world'


if __name__ == "__main__":
    app.run(debug=True, port=80)
