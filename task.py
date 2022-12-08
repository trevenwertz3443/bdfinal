"""
functions related to order table
"""
import db
import settings


_TABLE_NAME = 'order'

def create_table():
	conn = db.create_connection(settings.DB_NAME)
	sql = f"""
					-- order table
					CREATE TABLE IF NOT EXISTS {_TABLE_NAME} (
						id integer PRIMARY KEY,
						creation_date text NOT NULL,
						project_id integer NOT NULL
						priority integer,
						customer integer NOT NULL,
						status_id integer NOT NULL
					);
					"""
	with conn:
		success = db.create_table(conn, sql)
		if success:
			print('Order table created successfully!')
		else:
			print("Order table couldn't be created!")

def insert_order(order:tuple):
  sql = f"""
          INSERT INTO {_TABLE_NAME}(creation_date, priority, customer, status_id, project_id)
          VALUES(?,?,?,?,?);
        """

  conn = db.create_connection(settings.DB_NAME)
  with conn:
    cur = conn.cursor()
    cur.execute(sql, order)

def update_order(order:tuple):
	sql = f"""
				UPDATE {_TABLE_NAME} 
				SET priority = ?,
					creation_date
				WHERE id = ?
				"""
	conn = db.create_connection(settings.DB_NAME)
	with conn:
		cur = conn.cursor()
		cur.execute(sql, order)
	
def delete_order(order_id:tuple):
	sql = f"""
				DELETE FROM {_TABLE_NAME}
				WHERE id = ?
				"""
	conn = db.create_connection(settings.DB_NAME)
	with conn:
		cur = conn.cursor()
		cur.execute(sql, order_id)

def drop_table():
  conn = db.create_connection(settings.DB_NAME)
  sql = f"""
        DROP TABLE IF EXISTS {_TABLE_NAME};
        """
  with conn:
    cur = conn.cursor()
    cur.execute(sql)
    print(f'Table {_TABLE_NAME} dropped!')

def select_order(sql:str, para=None):
	conn = db.create_connection(settings.DB_NAME)
	rows = []
	headers = []
	if not para:
		para = ()
	with conn:
		cur = conn.cursor()
		cur.execute(sql, para)
		rows = cur.fetchall()
		headers = cur.description
	return headers, rows

def main():
	project_id = 1
	order_1 = ('Analyze the requirements of the app', project_id, 1, '2017-08-11', 1)
	order_2 = ('Confirm with user about the top requirements', project_id, 1, '2017-08-13', 2)
	insert_order(order_1)
	insert_order(order_2)

def test_update_order():
	order_id = 1
	creation_date = '2017-08-11'
	priority = 2
	order = (priority, creation_date, order_id)
	update_order(order)
	print("Order updated successfully!", order_id)

def test_delete_order():
	order_id = 1
	delete_order((order_id,))
	print(f'Order id: {order_id} deleted successfully!')

def select_order(sql:str):
	conn = db.create_connection(settings.DB_NAME)
	cur = conn.cursor()
	cur.execute(sql)
	rows = cur.fetchall()
	return rows

def test_select_order():
	sql = f"""
				SELECT * FROM {_TABLE_NAME};
				"""
	rows = select_order(sql)
	for row in rows:
		print(row)
	print('=======')
	sql = f"""
				SELECT * FROM {_TABLE_NAME}
				WHERE id = 2;
				"""
	rows = select_order(sql)
	for row in rows:
		print(row)

if __name__ == "__main__":
	test_select_order()