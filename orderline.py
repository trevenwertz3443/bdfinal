"""
functions related to orderline table
"""
import db
import settings

_TABLE_NAME = "orderline"

def create_table():
  conn = db.create_connection(settings.DB_NAME)
  with conn:
    sql = """
          CREATE TABLE IF NOT EXISTS %s (
            id integer primary key,
            order text NOT NULL,
            product text NOT NULL,
            quantity integer NOT NULL,
            price integer NOT NULL
          );
          """%(_TABLE_NAME)

    success = db.create_table(conn, sql)
    if success:
      print('Orderline table created successfully!')
    else:
      print('Orderline table could not be created!')

def insert_table(orderline:tuple):
  sql = f"""
        INSERT INTO {_TABLE_NAME}(order, product, quantity, price) VALUES 
        (?, ?, ?, ?);
        """
  conn = db.create_connection(settings.DB_NAME)
  projectid = None
  with conn:
    try:
      cursor = conn.cursor()
      cursor.execute(sql, orderline)
      conn.commit()
      projectid = cursor.lastrowid
      print('Orderline inserted successfully...')
    except Exception as ex:
      print("Error: ", ex, sql, orderline)

  return projectid

def drop_table():
  conn = db.create_connection(settings.DB_NAME)
  sql = f"""
        DROP TABLE IF EXISTS {_TABLE_NAME};
        """
  with conn:
    cur = conn.cursor()
    cur.execute(sql)
    print(f'Table {_TABLE_NAME} dropped!')

def main():
  create_table()
  project = ("ol", "phone", 2, 1190)
  pid = insert_table(project)
  print('orderline id: ', pid)
  #drop_table()

def select_project(sql:str):
	conn = db.create_connection(settings.DB_NAME)
	rows = []
	headers = []
	with conn:
		cur = conn.cursor()
		cur.execute(sql)
		rows = cur.fetchall()
		#cur.execute(sql)
		headers = cur.description
	return headers, rows

if __name__ == "__main__":
  main()