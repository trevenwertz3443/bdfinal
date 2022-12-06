__author__="Treven Wertz"
__date__ = "Dec 12, 2022"

"""
DB module 
- contains utility functions to work with sqlite db
"""
import sqlite3

# create_connection function
def create_connection(db_file: str):
  """
  function to connect to a sqlite db with given file db_file
  db_file: database file name
  return: None or conn
  """
  conn = None
  try:
    conn = sqlite3.connect(db_file)
    #print('Connection successful...')
  except Exception as ex:
    print('Error: ', ex, db_file)
  return conn

def create_table(conn, sql:str) -> bool:
  """
  conn: sqlite connnection object
  sql: create table sql string
  return: True if table created successfully, False otherwise
  """
  try:
    cursor = conn.cursor()
    cursor.execute(sql)
    return True
  except Exception as ex:
    print('Error:', ex, sql)
    return False


if __name__ == "__main__":
  pass