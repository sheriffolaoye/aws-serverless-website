import pymysql
import rds_config

class Database(object):
    def __init__(self):
        self.db_username = rds_config.db_username
        self.db_host = rds_config.db_endpoint
        self.db_name = rds_config.db_name
        self.db_password = rds_config.db_password
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
            query = "REPLACE INTO RepositoryData (ID, Name, Description, HtmlLink, Language, DateCreated) VALUES "

            for i in range(len(data)):
                values = "({}, '{}', '{}', '{}', '{}', STR_TO_DATE('{}', '%Y-%m-%dT%H:%i:%sZ'))"\
                        .format(data[i]["id"], data[i]["name"], data[i]["description"], 
                            data[i]["url"], data[i]["language"], data[i]["date"])
                if i + 1 < len(data):
                    values += ", "
                query += values

            self.cursor.execute(query)
            self.connection.commit()

    def removeDeleted(self, ids):
        if self.connection:
            query = "SELECT ID FROM RepositoryData"
            self.cursor.execute(query)
            original = self.cursor.fetchall()
            x = []
            for i in original:
                x.append(i[0])

            # get IDs of deleted repository entries
            toRemove = list(set(x) - set(ids))

            if len(toRemove) > 0:
                for i in toRemove:
                    query = "DELETE FROM RepositoryData WHERE ID = {}".format(i)
                    self.cursor.execute(query)
                    self.connection.commit()

    def close(self):
        if self.connection:
            self.connection.close()
