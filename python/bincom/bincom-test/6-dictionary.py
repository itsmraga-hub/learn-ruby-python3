# Write a program that uses a dictionary that contains ten usernames and passwords.
# The program should ask the user to enter their username and password.
# If the username is not in the dictionary, the program should indicate that the person is not a valid user of the system.
# If the username is in the dictionary, but the user does not enter the right password, the program should say that the password is invalid.
# If the password is correct, then the program should tell the user that they are now logged in to the system.

users = {
    "william": "password",
    "raga": "12345678",
    "will": "asdfghjkl",
    "user": "qwertyuiop",
    "mash": "passwd",
    "machaa": "zxcvbnm",
    "user_0": "87654321",
    "ragauser": "lkjhgfdsa",
    "willraga": "poiuytrewq",
    "willam": "mnbvcxzla",
}


def main(user_dict):
    username = input("Username: ")
    passwd = input("Password: ")

    if username in user_dict.keys():
        if user_dict[username] == passwd:
            print("You are now logged in to the system.")
        else:
            print("Invalid password")
    else:
        print("Not a valid user of the system. Register first!")


if __name__ == "__main__":
    main(user_dict=users)
