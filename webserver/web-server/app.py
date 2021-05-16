from flask import Flask, render_template, redirect, url_for
import urllib.request
import json
from database import Database
import datetime

app = Flask(__name__)

HOME = "index.html"
PROJECT = "projects.html"

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
    return redirect(url_for('projects'))
    
@app.route("/projects")
def projects():
    repos= None
    db = Database()

    if db.connect():
        repos = beautify(db.getRepos())

    return render_template(PROJECT, projects=repos)
