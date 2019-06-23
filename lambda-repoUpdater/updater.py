import urllib.request
import json
from database import Database
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

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
        repo_data = []

        # create Database instance
        self.db = Database()
        # Connect to the database
        if self.db.connect():
            for repo in self.repositories:
                ids.append(repo['id'])

                repo_data.append({
                "id" : repo['id'],
                "name" : repo['name'],
                "description" : repo['description'],
                "url" : repo['html_url'],
                "date" : repo['created_at'],
                "language" : repo['language']})

            self.db.update(repo_data)
            self.db.removeDeleted(ids)
            # close connection
            self.db.close()

            return True
        else:
            logger.info("Cannot connect to database")
            return False
