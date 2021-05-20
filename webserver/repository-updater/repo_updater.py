import urllib.request
import json
from database import Database
import os
import logging
from datetime import datetime

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')

class RepoUpdater(object):
    def last_update_time(self):
        self.db = Database()

    def update(self):
        link = os.getenv("REPO_LINK")
        request_data = urllib.request.urlopen(link)
        json_data = json.loads(request_data.read())
        
        repositories = []
        date_format = "%Y-%m-%dT%H:%M:%SZ"

        for repo in json_data:
            unformatted_date = datetime.strptime(repo['created_at'], date_format)
            formatted_date = unformatted_date.strftime("%H:%M on %b %d, %Y")

            repositories.append({
                "name" : repo['name'],
                "description" : repo['description'],
                "url" : repo['html_url'],
                "date_created" : formatted_date,
                "language" : repo['language']}
                )

        self.db = Database()
        return self.db.update_repository_data(repositories)

def main():
    repoUpdater = RepoUpdater()
    repoUpdater.update()

if __name__=="__main__":
    main()