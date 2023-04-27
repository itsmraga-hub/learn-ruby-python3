# Write a program that asks the user to enter a password. If the user enters the right password, the program should tell them they are logged in to the system.
# Otherwise, the program should ask them to renter the password.
# The user should only get five tries to enter the password, after which point the program should tell them that they are kicked off the system.

passwd_count = 5

def main(passwd_count=passwd_count):
    passwd = '12345678'

    user_name = input("User name: ")
    user_password = input(
            "Hi, " + user_name + " please input your password to access the system: ")
    while passwd_count:
        passwd_count -= 1
        if passwd_count == 0:
            break
        if user_password == passwd:
            print("Hi " + user_name + ", Welcome to the system")
            break
        else:
            print("You have " + str(passwd_count) + " tries remaining!!!\n\n")
            user_password = input(
            "Hi, " + user_name + " please input your password to access the system: ")

    if passwd_count < 1:
        print("System exit")
        exit()
    else:
        print("You are now Logged in!!!")
        print("Have fun using the system")


if __name__ == "__main__":
    main()
