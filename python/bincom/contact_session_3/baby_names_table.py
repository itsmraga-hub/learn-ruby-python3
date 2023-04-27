import psycopg2

# establishing the connection
conn = psycopg2.connect(
   database="todo_list", user='postgres', password='12345678', host='127.0.0.1', port= '5432'
)
conn.autocommit = True

cursor = conn.cursor()

# sql_create_db = '''CREATE database todo_list'''

sql_create_table = '''CREATE TABLE baby_names (
    id SERIAL PRIMARY KEY,
    name TEXT
);
'''

# Creating a database
# cursor.execute(sql_create_db)
# print("Database created successfully...")

conn = psycopg2.connect(database="todo_list", user="postgres", password="12345678")

cursor = conn.cursor()

# Creating a table
cursor.execute(sql_create_table)
print("Table created successfully...")
conn.commit()

conn.close()