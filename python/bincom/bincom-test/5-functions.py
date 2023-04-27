# Write a function that takes two strings as arguments and returns how many matches there are between the strings.
# A match is where the two strings have the same character at the same index.
# For instance, 'python' and 'path' match in the first, third and fourth characters, so the function should return 3.

def check_str_match(str_1, str_2):
    str_1_len = len(str_1)
    str_2_len = len(str_2)
    count = 0

    if str_1_len <= str_2_len:
        for i, l in enumerate(str_1):
            for j, l2 in enumerate(str_2):
                if i == j and l == l2:
                    count += 1

        print(count)
        return count
    else:
        for i, l in enumerate(str_2):
            for j, l2 in enumerate(str_1):
                if i == j and l == l2:
                    count += 1
        print(count)
        return count


def main():
    check_str_match(str_1="william", str_2="william")
    check_str_match(str_1="python", str_2="path")


if __name__ == "__main__":
    main()
