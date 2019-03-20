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
	# list to store id's to remove deleted repositories
        ids = []
        # create Database instance
        self.db = Database()
        # Connect to the database
        if self.db.connect():
            for repo in self.repositories:
                id = repo['id']
                ids.append(id)
                name = repo['name']
                description = repo['description']
                url = repo['html_url']
                date = repo['created_at']
                language = repo['language']
                self.db.update(id, name, description, url, language, date)
            self.db.removeDeleted(ids)
            # close connection
            self.db.close()
            return True
        else:
            print("failed to update repositories")
            return False
