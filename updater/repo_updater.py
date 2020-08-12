import urllib.request
import json
from database import Database
from datetime import datetime

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
        self.db = Database("RepositoryData")
        # Connect to the database
        
        for repo in self.repositories:
            repo_data.append({
            "id" : str(repo['id']),
            "name" : repo['name'],
            "description" : repo['description'],
            "url" : repo['html_url'],
            "date" : repo['created_at'],
            "language" : repo['language']})

        return self.db.updateRepos(repo_data)

def main():
    repoUpdater = RepoUpdater()
    
    current_time = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ%f')[:-3]
    print(current_time + " | INFO | Attempting to update repositories")
    
    if repoUpdater.update():
        print(current_time + " | INFO | Updated repositories")
    else:
        print(current_time + " | ERROR | Failed to update repositories")

if __name__=="__main__":
    main()

    
