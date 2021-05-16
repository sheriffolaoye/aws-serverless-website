import pymysql
import os

class Database(object):
	def __init__(self):
		self.db_port = 3306
		if os.getenv("DB_PORT"):
			self.db_port = int(os.getenv("DB_PORT"))
		self.db_username = os.getenv("DB_USERNAME")
		self.db_host = os.getenv("DB_ENDPOINT")
		self.db_name = os.getenv("DB_NAME")
		self.db_password = os.getenv("DB_PASSWORD")

		self.connection = None

	def connect(self):
		self.connection = pymysql.connect(host=self.db_host,
						user=self.db_username,
						db=self.db_name,
			   			password=self.db_password,
						port=self.db_port)
		try:
			self.cursor = self.connection.cursor()
			return True
		except:
			return False

	def getRepos(self):
		if self.connect():
			query = """SELECT Name, DateCreated, Description, URL, 
			           Language FROM RepositoryData ORDER BY DateCreated DESC"""
			repos = []
			try:
				self.cursor.execute(query)
				repos = self.cursor.fetchall()
			except:
				pass
			return repos

	def close(self):
		if self.connection:
			self.connection.close()

