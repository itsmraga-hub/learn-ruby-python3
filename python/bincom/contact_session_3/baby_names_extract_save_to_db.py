import re
import psycopg2
""""
    A name extract in python to read my name from a file and write the names to the terminal
"""

# establishing the connection
conn = psycopg2.connect(
    database="todo_list", user='postgres', password='12345678', host='127.0.0.1', port='5432'
)

cursor = conn.cursor()

path = 'python/bincom/contact_session_2/baby2008.html'
# path = 'python/bincom/contact_session_3/file.html'

try:
    with open(path, 'r') as f:
        baby_file = f.read()  # or f.read() because its only one name
        # pattern = r'<td>(.*?)</td>'
        pattern = r'<td>([A-Za-z]+)</td>'
        names = re.findall(pattern, baby_file)
        # match = re.search(pattern, baby_file)
        for name in names:
            sql = f"INSERT INTO baby_names (name) VALUES ('{name}')"
            cursor.execute(sql)
            conn.commit()

        # print(baby_file)
except FileNotFoundError:
    raise FileNotFoundError("file not found")
