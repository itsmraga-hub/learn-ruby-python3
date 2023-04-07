import psycopg2

# Connect to the todolist database
conn = psycopg2.connect(database="todo_list", user="postgres", password="$AFfil!at0r$")

def add_todo_item(task):
    cur = conn.cursor()
    sql = f"INSERT INTO items (task) VALUES ('{task}')"
    cur.execute(sql)
    conn.commit()
    print("Item added.")

def delete_todo_item(id):
    cur = conn.cursor()
    sql = "DELETE FROM items WHERE id={}".format(id)
    cur.execute(sql)
    conn.commit()
    print("Item deleted.")

def list_todo_items():
    cur = conn.cursor()
    sql = "SELECT * FROM items"
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        print(f"{row[0]}. {row[1]}")

while True:
    print("\nWelcome to Today's To Do List")
    print("\tMENU")
    print("\t1. Add Todo list item")
    print("\t2. Delete ToDo item")
    print("\t3. List Todo list")
    print("\tPress 4 or 'Q' at any time to exit\n")
    command = input("Enter a menu number: ")
    if command == "1":
        todo = input("Enter todo item: ")
        add_todo_item(todo)
    elif command == "2":
        id = input("Enter item ID: ")
        delete_todo_item(id)
    elif command == "3":
        list_todo_items()
    elif command == "q" or command == "Q" or command == "4":
        break
    else:
        print("Invalid command.")
