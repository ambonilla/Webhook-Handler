#!/usr/bin/env python

import mysql.connector
from config import config

class mysql_handler:

   def __init__(self):
      try:
         new_config = config()
         self.cnx = mysql.connector.connect(user= new_config.db_user,
               password= new_config.db_pwd,
               host='127.0.0.1',
               database=new_config.db_name
               )

      except mysql.connector.Error as err:
         if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
         elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
         else:
            print(err)

   def create_table(self):
      str_query = ("CREATE TABLE IF NOT EXISTS issues("
            "id INT NOT NULL AUTO_INCREMENT, "
            "issue_id VARCHAR(64) NOT NULL UNIQUE, "
            "issue_title VARCHAR(64), "
            "issue_description VARCHAR(128), "
            "PRIMARY KEY (id) ) "
            "COLLATE = utf8_bin;")

      cursor = self.cnx.cursor()
      try:
         cursor.execute(str_query)

      except mysql.connector.Error as err:
         print err.msg

      finally:
         cursor.close()
         self.cnx.close()




   def add_new_issue(self, id_num, title=None, description=None):
      str_query = ("INSERT INTO issues "
            "(issue_id, issue_title, issue_description) "
            "VALUES (%s,%s,%s)")
      try:
         cursor = self.cnx.cursor()
         cursor.execute(str_query, (id_num, title, description))
         self.cnx.commit()
      except mysql.connector.Error as err:
         print("Failed INSERT INTO issues: {}".format(err))
         exit(1)
      finally:
         cursor.close()
         self.cnx.close()

   def close_issue(self, id_num):
      str_query = "DELETE FROM issues WHERE issue_id = %s"
      try:
         cursor = self.cnx.cursor()
         cursor.execute(str_query, (id_num,))
         self.cnx.commit()
      except mysql.connector.Error as err:
         print("Failed DELETE FROM issues: {}".format(err))
         exit(1)
      finally:
         cursor.close()
         self.cnx.close()

   def verify_issue(self, id_num):
      str_query = "SELECT issue_title, issue_description FROM issues WHERE issue_id = %s"
      try:
         cursor = self.cnx.cursor()
         cursor.execute(str_query, (id_num,))
         row = cursor.fetchone()
      except mysql.connector.Error as err:
         print("Failed SELECT FROM issues: {}".format(err))
         exit(1)
      finally:
         cursor.close()
         return row

   def update_issue(self, id_num, title, description):
      str_query = "UPDATE issues SET issue_title = %s, issue_description = %s WHERE issue_id = %s"
      try:
         cursor = self.cnx.cursor()
         cursor.execute(str_query, (title, description, id_num))
         self.cnx.commit()
      except mysql.connector.Error as err:
         print("Failed UPDATE FROM issues: {}".format(err))
         exit(1)
      finally:
         cursor.close()
         self.cnx.close()

