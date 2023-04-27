def fibonacci(num):
    first_num = 0
    second_num = 1
    print(first_num)
    j = 1
    while j <= num:
        third_num = first_num + second_num
        print(second_num)
        j += 1
        first_num = second_num
        second_num = third_num


        
fibonacci(10)