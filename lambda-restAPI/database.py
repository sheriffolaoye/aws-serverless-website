import pymysql
import os
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

class Database(object):
	def __init__(self):
        self.db_username = os.environ["DB_USERNAME"]
        self.db_host = os.environ["DB_ENDPOINT"]
        self.db_name = os.environ["DB_NAME"]
        self.db_password = os.environ["DB_PASSWORD"]
		self.connected = False
		self.connection = None

	def connect(self):
		self.connection = pymysql.connect(host=self.db_host,
						  user=self.db_username,
						  db=self.db_name,
			   			 password=self.db_password,
						 connect_timeout=20
						)
		try:
			self.cursor = self.connection.cursor()
			self.connected = True
			return True
		except:
			return False

	def getRepos(self):
		if self.connected:
			query = """SELECT Name, DateCreated, Description, HtmlLink, 
			           Language FROM RepositoryData ORDER BY DateCreated DESC"""
			repos = []
			try:
				self.cursor.execute(query)
				repos = self.cursor.fetchall()
			except Exception as e:
				logger.info(e)
			return repos
		else:
			logger.log("Connect to Database first!")

	def close(self):
		if self.connection:
			self.connection.close()
