from flask import Flask
from flask import request
import requests

app = Flask(__name__)

@app.route("/api/rest")
def get_helloworld():
	url = 'http://dummyservice:5000/'
	r = requests.get(url)
	result = r.text
	return result


if __name__ == "__main__":
    app.run(debug = True, host = '0.0.0.0')
