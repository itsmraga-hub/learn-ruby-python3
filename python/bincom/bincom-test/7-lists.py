# Write a program that takes any two lists L and M of the same size and adds their elements together to form a new list N whose elements are sums of the corresponding elements in L and M.
# For instance, if L= [3, 1, 4 ] and M = [1, 5, 9], then N should equal [4, 6, 13]

def add_list_elements(l1, l2):
    output = []
    if len(l1) == len(l2):
        for i, num1 in enumerate(l1):
            for j, num2 in enumerate(l2):
                if i == j:
                    output.append(num1 + num2)
        print(output)
    else:
        print("Lists have to be of equal length")
    # return output


def main():
    add_list_elements(l1=[3, 1, 4], l2=[1, 5, 9])


if __name__ == "__main__":
    main()
