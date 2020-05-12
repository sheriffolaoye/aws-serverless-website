import json
import datetime
from database import Database
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def beautify(repositories):
    selectors = ["Name","DateCreated","Description","HtmlLink","Language"]
    repos = []
    for r in repositories:
         item = dict(zip(selectors, r))
         repos.append(item)
    for repo in repos:
        dateTime = repo["DateCreated"]
        repo["DateCreated"] = dateTime.strftime("%H:%M on %b %d, %Y")
    return repos

@app.route("/")
def get_repos():
    db = Database()
    repos = None

    if db.connect():
        repos = beautify(db.getRepos())

    return jsonify(repos)


if __name__=="__main__":
	app.run(host="0.0.0.0")
