import pymysql
import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

class Database(object):
    def __init__(self, table_name):
        self.db_username = os.environ["DB_USERNAME"]
        self.db_host = os.environ["DB_ENDPOINT"]
        self.db_name = os.environ["DB_NAME"]
        self.db_password = os.environ["DB_PASSWORD"]
        self.table_name = table_name
        self.connection = None


    def connect(self):
        self.connection = pymysql.connect(host=self.db_host,
                                          user=self.db_username,
                                          db=self.db_name,
                                          password=self.db_password,
                                          connect_timeout=5)
        try:
            self.cursor = self.connection.cursor()

            return True
        except:
            return False


    def updateRepos(self, data):
        if self.connect():
            query = "INSERT INTO RepositoryData(Id, Name, Description, URL, Language, DateCreated) VALUES "

            for i in range(len(data)):
                values = "('{}', '{}', '{}', '{}', '{}', STR_TO_DATE('{}', '%Y-%m-%dT%H:%i:%sZ'))"\
                        .format(data[i]["id"], data[i]["name"], data[i]["description"], 
                            data[i]["url"], data[i]["language"], data[i]["date"])
                if i + 1 < len(data):
                    values += ", "
                query += values

            query += " ON DUPLICATE KEY UPDATE Name=VALUES(Name), Description=VALUES(Description), \
                     URL=VALUES(URL), Language=VALUES(Language), DateCreated=VALUES(DateCreated)"

            self.cursor.execute(query)
            self.connection.commit()
            self.close()

            return True
        else:
            return False


    def updateVideos(self, data):
        if self.connect():
            query = "INSERT INTO VideoData(Id, Title, PublishTime) VALUES "

            for i in range(len(data)):
                values = "('{}', '{}', STR_TO_DATE('{}', '%Y-%m-%dT%H:%i:%sZ'))"\
                        .format(data[i]["id"], data[i]["title"], data[i]["publishTime"])
                if i + 1 < len(data):
                    values += ", "
                query += values

            query += " ON DUPLICATE KEY UPDATE Title=VALUES(Title), PublishTime=VALUES(PublishTime)"
            self.cursor.execute(query)
            self.connection.commit()
            self.close()

            return True
        else:
            return False


    def close(self):
        if self.connection:
            self.connection.close()
