import json
from updater import RepoUpdater

def main(event, context):
    repoUpdater = RepoUpdater()
    message = "success"

    # try to update the database
    if not repoUpdater.update():
        message = "failed to update repositories"

    # define JSON response
    response = {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*",},
            "body": json.dumps(message)}
    return response

if __name__=="__main__":
    main("","")
