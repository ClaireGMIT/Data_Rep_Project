import mysql.connector

class TabPrdnDAO:
    db=""
    def __init__(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="ROOT", #Password on local machine
            database="tablets"
        )
  
    def create