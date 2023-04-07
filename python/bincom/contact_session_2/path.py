import os

# print(dir(os))
# print(os.__doc__)
path = 'python\\bincom\contact_session_2\path.py'

abs_path = os.getcwd()
abs_path = os.path.join(abs_path, path)
print(abs_path)