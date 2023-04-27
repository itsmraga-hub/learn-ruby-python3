# Write a program that uses exactly for loops to print the sequence of the letters below.
# AAAAAAAAAABBBBBBBCDCDCDCDEFFFFFFG

def main():
    output = ''
    for i in range(1, 11):
        output += 'A'

    for i in range(1, 8):
        output += 'B'

    for i in range(1, 5):
        output += 'CD'

    output += 'E'

    for i in range(1, 7):
        output += 'F'

    output += 'G'

    print(output)


if __name__ == "__main__":
    main()
