from rejson import Client, Path
import datetime
import time
import logging
import sys
import os

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')

redis_connection_retries = 5
redis_retry_wait_time = 2

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
        except:
            return None

    def get_last_update_time(self):
        for i in range(1, redis_connection_retries+1):
            redis_connection = self.connect_to_redis()

            if redis_connection:
                update_time = redis_connection.jsonget('repository', Path("update_time"))
                #logging.info("Successfully updated repositories")
                return update_time
            else:
                logging.error("Error connecting to Redis, waiting for {} secs before connecting again. Retry {}/{}.".
                    format(redis_retry_wait_time, i, redis_connection_retries))
                time.sleep(redis_retry_wait_time)
        
        logging.error("Failed to update repositories because Redis could not be reached")
        return None

    def update_repository_data(self, repositories):
        for i in range(1, redis_connection_retries+1):
            redis_connection = self.connect_to_redis()

            if redis_connection:
                time = datetime.datetime.now()
                repository_data = {
                    "update_time" : str(time),
                    "repositories" : repositories
                }
                redis_connection.jsonset('repository', Path.rootPath(), repository_data)
                logging.info("Successfully updated repositories")

                return
            else:
                logging.error("Error connecting to Redis, waiting for {} secs before connecting again. Retry {}/{}.".
                    format(redis_retry_wait_time, i, redis_connection_retries))
                time.sleep(redis_retry_wait_time)
        
        logging.error("Failed to update repositories because Redis could not be reached")
        return