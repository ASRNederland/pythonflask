from flask import Flask
from flask import request
import requests

app = Flask(__name__)

@app.route("/")
def get_helloworld():
	result = "Hello world! This is a Python app."
	return result

if __name__ == "__main__":
    app.run(debug = True, host = '0.0.0.0')
