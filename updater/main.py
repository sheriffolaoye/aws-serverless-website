import json
from updater import RepoUpdater
from datetime import datetime

def main():
    repoUpdater = RepoUpdater()
    return repoUpdater.update()

if __name__=="__main__":
    current_time = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ%f')[:-3]
    print(current_time + " | INFO | Attempting to update repositories")
    
    current_time = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ%f')[:-3]
    if main():
        print(current_time + " | INFO | Updated repositories")
    else:
        print(current_time + " | ERROR | Failed to update repositories")
