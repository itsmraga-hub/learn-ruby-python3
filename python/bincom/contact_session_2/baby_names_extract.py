import re
""""
    A name extract in python to read my name from a file and write the names to the terminal
"""

path = 'python/bincom/contact_session_2/baby2008.html'

try:
    with open(path, 'r') as f:
        baby_file = f.read() # or f.read() because its only one name
        # pattern = r'<td>(.*?)</td>'
        pattern = r'<td>([A-Za-z]+)</td>'
        names = re.findall(pattern, baby_file)
        # match = re.search(pattern, baby_file)
        for i in range(len(names)):
            print("{}: {}".format(i, names[i]))

        # print(baby_file)
except FileNotFoundError:
    raise FileNotFoundError("file not found")