from flask import Flask, redirect, url_for, request
import requests
import sys
import json
import hashlib

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def hello():
	if request.method == "POST":
		jsonObject = request.json

		print(jsonObject)

		message = jsonObject["md5"]

		h = hashlib.new("md5")
		h.update(str.encode(message))

		print(h.hexdigest())
		#return redirect(url_for("hashed"))
		return "Flask dockerizeddddddd"
	else:
		return "Flask dockerizeddddddd"

@app.route("/hashed")
def hashed():
	return "hashed"

if __name__ == "__main__":
	app.run(debug=True)
