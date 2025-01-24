import mysql.connector as mysql_connector
from dotenv import load_dotenv
import os


load_dotenv()

class MySQLDatabase:
    
    def __init__(self):
        self._host = os.getenv("HOST")
        self._username = os.getenv("USERNAME")
        self._passwd = os.getenv("PASSWD")
        self._database = os.getenv("DATABASE")
        self._conn = self._connecting()

    def _connecting(self):
        return mysql_connector.connect(
            user = self._username,
            password = self._passwd,
            host = self._host,
            datbase = self._database
        )

def querying(self, query):
    if not self.conn.is_connected():
        self._connect()

             
    