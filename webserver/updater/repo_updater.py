import urllib.request
import json
from database import Database
import os
import logging

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')

class RepoUpdater(object):
    def update(self):
        link = os.getenv("REPO_LINK")
        self.data = urllib.request.urlopen(link)
        self.json_data = self.data.read()
        self.repositories = json.loads(self.json_data)
        
        self.db = Database()
        repo_data = []

        for repo in self.repositories:
            repo_data.append({
                "id" : str(repo['id']),
                "name" : repo['name'],
                "description" : repo['description'],
                "url" : repo['html_url'],
                "date" : repo['created_at'],
                "language" : repo['language']}
                )

        return self.db.updateRepos(repo_data)

def main():
    repoUpdater = RepoUpdater()
    
    if repoUpdater.update():
        logging.info("Successfully updated repositories")
    else:
        logging.error("Failed to update repositories")

if __name__=="__main__":
    main()