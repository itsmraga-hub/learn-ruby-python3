# Write a program that asks the user ti enter a word and determines whether the word is a palindrome or not.
# A palindrome is a word that reads the same backwards as forwards.

def main():
    word = input("Enter the word: ")
    reversed_word = word[::-1]
    if word == reversed_word:
        print("The word is a palindrome.")
    else:
        print("The word is not a palindrome.")


if __name__ == "__main__":
    main()
