from flask import Flask, render_template, redirect, url_for
from datetime import datetime
import urllib.request
import json
from database import Database

app = Flask(__name__)

HOME = "index.html"
PROJECT = "projects.html"

@app.route("/")
def home():
    return redirect(url_for('projects'))
    
@app.route("/projects")
def projects():
    db = Database()
    repositories = db.get_repository_data()
    return render_template(PROJECT, projects=repositories)