# Write a program that asks the user how many credits they have taken.
# If they have taken 23 or less, print that the student is a freshman.
# If they have taken between 24 and 53, print that theu are a sophomore.
# The range for juniors is 54 to 83, and for seniors it is 84 and over.

def main():
    num_of_credits = input("How many credits have you taken: ")

    try:
        num_of_credits = int(num_of_credits)
        output = 'The student is a '
        if num_of_credits > 84:
            print(output + 'senior.')
        elif num_of_credits >= 54 and num_of_credits < 84:
            print(output + 'junior.')
        elif num_of_credits > 23 and num_of_credits < 55:
            print(output + 'sophomore.')
        elif num_of_credits < 23:
            print(output + 'freshman.')
    except:
        raise(ValueError("number of credits has to be an int"))


if __name__ == "__main__":
    main()
