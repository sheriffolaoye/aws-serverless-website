import requests
import json
from database import Database
from datetime import datetime
from dotenv import load_dotenv
import os

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

class VideoUpdater(object):
    def __init__(self):
        self.link = "https://www.googleapis.com/youtube/v3/search"
        self.params = {
            "channelId"     : os.getenv("CHANNEL_ID"),
            "key"           : os.getenv("YOUTUBE_API_KEY"),
            "part"          : "snippet",
            "maxResults"    : 50,
            "type"          : "video"
        }

    def update(self):
        response = requests.get(self.link, self.params)
        data = json.loads(response.text)
        video_data = []
        data = data['items']

        for i in data:
            video_data.append({
                'id'            : i['id']['videoId'],
                'title'         : i['snippet']['title'],
                'publishTime'   : i['snippet']['publishTime']
            })

        self.db = Database()
        return self.db.updateVideos(video_data)


def main():
    updater = VideoUpdater()

    current_time = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ%f')[:-3]
    print(current_time + " | INFO | Attempting to update repositories")
    
    if updater.update():
        print(current_time + " | INFO | Updated videos successfully")
    else:
        print(current_time + " | ERROR | Failed to update videos")


if __name__=="__main__":
    main()