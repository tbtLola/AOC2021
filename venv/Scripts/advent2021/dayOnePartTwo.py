#pt 2
def get_number_of_three_increases(input):
    inc_num = 0
    three_sum_input = []
    for i in range(len(input)):
        three_sum = input[i:i+3]
        if (len(three_sum) == 3):
            three_sum = sum(three_sum)
            three_sum_input.append(three_sum)
    get_number_of_increases(three_sum_input)

#pt 1
def get_number_of_increases(input):
    inc_num = 0
    for i in range(len(input)):
        if i + 1 < len(input):
            if input[i + 1] > input[i]:
                inc_num = inc_num + 1
    print(inc_num)

if __name__ == '__main__':
    get_number_of_three_increases([199, 200, 208, 210, 200, 207, 240, 269, 260, 263])
