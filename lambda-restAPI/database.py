import pymysql
import rds_config
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

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
