from flask import Flask, render_template
import urllib.request
import json
from database import Database
import datetime


app = Flask(__name__)

HOME = "index.html"
PROJECT = "projects.html"
VIDEO = "videos.html"

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
def home():
    return render_template(HOME)
    
@app.route("/projects")
def projects():
    repos= None
    db = Database()

    if db.connect():
        repos = beautify(db.getRepos())

    return render_template(PROJECT, projects=repos)

@app.route("/videos")
def videos():
    db = Database()
    videos = db.getVideos()

    return  render_template(VIDEO, videos=videos)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
