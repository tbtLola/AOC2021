def get_number_of_increases(input):
    inc_num = 0
    for i in range(len(input)):
        if i + 1 < len(input):
            if input[i + 1] > input[i]:
                inc_num = inc_num + 1
    print(inc_num)