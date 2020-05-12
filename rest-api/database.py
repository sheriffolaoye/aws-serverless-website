import pymysql
import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

class Database(object):
	def __init__(self):
		self.connected = False
		self.connection = None
		self.db_username = os.getenv("DB_USERNAME")
		self.db_host = os.getenv("DB_ENDPOINT")
		self.db_name = os.getenv("DB_NAME")
		self.db_password = os.getenv("DB_PASSWORD")

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
			return False

	def getRepos(self):
		if self.connected:
			query = """SELECT Name, DateCreated, Description, URL, 
			           Language FROM RepositoryData ORDER BY DateCreated DESC"""
			repos = []
			try:
				self.cursor.execute(query)
				repos = self.cursor.fetchall()
			except Exception as e:
				logger.info(e)
			return repos

	def close(self):
		if self.connection:
			self.connection.close()

