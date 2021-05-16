import pymysql
import os
import time
import logging
import sys

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')

db_connection_retries = 5
db_retry_wait_time = 2

class Database(object):
    def __init__(self):
        self.db_port = 3306
        if os.getenv("DB_PORT"):
            self.db_port = int(os.getenv("DB_PORT"))

        self.db_username = os.getenv("DB_USERNAME")
        self.db_host = os.getenv("DB_ENDPOINT")
        self.db_name = os.getenv("DB_NAME")
        self.db_password = os.getenv("DB_PASSWORD")

    def connect(self):
        # retries = 5
        for i in range(1, db_connection_retries+1):
            db_connection = self.db_connection_handler()

            if db_connection:
                return db_connection
            else:
                logging.error("Error connecting to DB, waiting for {} secs before connecting again. Retry {}/{}.".
                    format(db_retry_wait_time, i, db_connection_retries))
                time.sleep(db_retry_wait_time)
        logging.error("Gave up when connecting to DB")
        
        return sys.exit()

    def db_connection_handler(self):
        try:
            connection = pymysql.connect(host=self.db_host,
                                          user=self.db_username,
                                          db=self.db_name,
                                          password=self.db_password,
                                          port=self.db_port,
                                          connect_timeout=5)

            return connection
        except:
            return None

    def updateRepos(self, data):
        connection = self.connect()
        query = "INSERT INTO RepositoryData(Id, Name, Description, URL, Language, DateCreated) VALUES "

        for i in range(len(data)):
            values = "('{}', '{}', '{}', '{}', '{}', STR_TO_DATE('{}', '%Y-%m-%dT%H:%i:%sZ'))"\
                        .format(data[i]["id"], data[i]["name"], data[i]["description"],
                            data[i]["url"], data[i]["language"], data[i]["date"])
            if i + 1 < len(data):
                values += ", "
            query += values

        query += " ON DUPLICATE KEY UPDATE Name=VALUES(Name), Description=VALUES(Description), URL=VALUES(URL), Language=VALUES(Language), DateCreated=VALUES(DateCreated)"

        try:
            cursor = connection.cursor()
            cursor.execute(query)
            connection.commit()
            connection.close()

            return True
        except Exception as e:
            logging.exception(str(e))
            return False