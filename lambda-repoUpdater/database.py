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
                                          connect_timeout=20)
        try:
            self.cursor = self.connection.cursor()
            self.connected = True
            return True
        except:
            raise "connection error!"
            return False

    def update(self, id, name, description, url, language, date):
        if self.connected:
            query = """INSERT IGNORE INTO RepositoryData (ID, Name, Description, 
                       HtmlLink, Language, DateCreated) VALUES ({}, '{}', '{}', 
                       '{}', '{}', STR_TO_DATE('{}', '%Y-%m-%dT%H:%i:%sZ'))
                    """.format(id, name, description, url, language, date)
            self.cursor.execute(query)
            self.connection.commit()
        else:
            print("Connect to Database first!")

    def getRepos(self):
        if self.connected:
            query = """SELECT Name, DateCreated, Description, 
                       HtmlLink, Language FROM RepositoryData"""
            repos = []
            try:
                self.cursor.execute(query)
                repos = self.cursor.fetchall()
            except Exception as e:
            	repos.append(e)
            return repos
        else:
            print("Connect to Database first!")

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
        else:
            print("Nothing to close!")

    def close(self):
        if self.connection:
            self.connection.close()
        else:
            print("Nothing to close!")
