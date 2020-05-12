import urllib.request
import json
from database import Database

class RepoUpdater(object):
    def __init__(self):
        self.link = "https://api.github.com/users/sheriffolaoye/repos"

    def update(self):
        # get repositories from the GitHub API
        self.data = urllib.request.urlopen(self.link)
        self.json_data = self.data.read()
        self.repositories = json.loads(self.json_data)
	    
        repo_data = []

        # create Database instance
        self.db = Database()
        # Connect to the database
        if self.db.connect():
            for repo in self.repositories:
                repo_data.append({
                "id" : str(repo['id']),
                "name" : repo['name'],
                "description" : repo['description'],
                "url" : repo['html_url'],
                "date" : repo['created_at'],
                "language" : repo['language']})

            self.db.update(repo_data)
            self.db.close()

            return True
        else:
            print("Cannot connect to database")
            return False
