import pymysql
import os

class Database(object):
    def __init__(self):
        self.db_username = os.environ["DB_USERNAME"]
        self.db_host = os.environ["DB_ENDPOINT"]
        self.db_name = os.environ["DB_NAME"]
        self.db_password = os.environ["DB_PASSWORD"]
        self.table_name = os.environ["DB_TABLE_NAME"]
        self.connected = False
        self.connection = None


    def connect(self):
        self.connection = pymysql.connect(host=self.db_host,
                                          user=self.db_username,
                                          db=self.db_name,
                                          password=self.db_password,
                                          connect_timeout=5)
        try:
            self.cursor = self.connection.cursor()
            self.connected = True

            return True
        except:
            return False


    def update(self, data):
        if self.connected:
            query = "INSERT INTO {}(Id, Name, Description, URL, Language, DateCreated) VALUES ".format(self.table_name)

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


    def close(self):
        if self.connection:
            self.connection.close()
