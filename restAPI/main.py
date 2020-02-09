import json
import datetime
from database import Database
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

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

def main(event,context):
    db = Database()
    if db.connect():
        repos = db.getRepos()
        repos = beautify(repos)
    else:
        logger.info("Cannot connect to database")

    response = {
        "statusCode": 200,
        "headers": {
                "Access-Control-Allow-Origin": "*",},
        "body": json.dumps(repos)}

    return response

# for local testing
#if __name__=="__main__":
#	main(None,None)
