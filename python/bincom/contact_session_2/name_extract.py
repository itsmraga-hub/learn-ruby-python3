""""
    A name extract in python to read my name from a file and write the names to the terminal
"""

path = 'python/bincom/contact_session_2/name.txt'

try:
    with open(path, 'r') as f:
        name = f.readline() # or f.read() because its only one name
        names = name.split(" ")
        print("First name: {}\nMiddle name: {}\nLast name: {}".format(names[0], names[1], names[2]))
except FileNotFoundError:
    raise FileNotFoundError("file not found")