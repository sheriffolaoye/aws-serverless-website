from flask import Flask, render_template, redirect
import urllib.request
import json

app = Flask(__name__)

HOME = "index.html"
PROJECT = "projects.html"
RESTAPI_URL = "http://rest.sheriffolaoye.com"

@app.route("/")
def home():
    return render_template(HOME)
    
@app.route("/projects")
def projects():
    repositories = None

    try:
        data = urllib.request.urlopen(RESTAPI_URL)
        json_data = data.read()
        repositories = json.loads(json_data)
    except:
        pass

    return render_template(PROJECT, projects=repositories)

if __name__ == "__main__":
    app.run(host="0.0.0.0")