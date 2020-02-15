import json
from updater import RepoUpdater
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def main():
    logger.info("")
    repoUpdater = RepoUpdater()
    message = "Repositories updated successfully!"

    # try to update the database
    if not repoUpdater.update():
        # do some logging
        message = "Failed to update repositories"

    logger.info(message)

    # define JSON response
    response = {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*",},
            "body": json.dumps(message)}
    return response

# for local testing
if __name__=="__main__":
    main()
