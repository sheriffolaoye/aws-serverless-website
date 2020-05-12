import json
from updater import RepoUpdater

def main():
    repoUpdater = RepoUpdater()
    message = "Repositories updated successfully!"

    if not repoUpdater.update():
        message = "Failed to update repositories"

    print(message)

if __name__=="__main__":
    main()
