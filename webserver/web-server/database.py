from rejson import Client, Path
import logging
import os

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')

class Database():
    def __init__(self):
        self.redis_port = 6379
        if os.getenv("REDIS_PORT"):
            self.redis_port = int(os.getenv("REDIS_PORT"))
        self.redis_host = os.getenv("REDIS_HOST")

    def connect_to_redis(self):
        try:
            redis_json_client = Client(host=self.redis_host, port=self.redis_port, decode_responses=True)
            return redis_json_client
        except Exception as e:
            logging.error(str(e))
            return None
            
    def get_repository_data(self):
        redis_connection = self.connect_to_redis()

        if redis_connection:
            repositories = redis_connection.jsonget("repository", Path("repositories"))
            return repositories
        else:
            logging.error("Unable to get repository data")
            return None
