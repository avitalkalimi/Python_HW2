# *************** HOMEWORK 2 ***************
# GOOD LUCK!

# ************************ QUESTION 1 **************************
### WRITE CODE HERE
def rhombus(side_size):  # print rhombus by side size he get
    spaces_left_up = (side_size - 1)
    asterisk_up = (side_size - side_size + 1)
    spaces_right_up = (side_size - 1)
    while spaces_left_up > -1:  # print the upper triangle
        print((spaces_left_up * " ") + (asterisk_up * "*"))
        spaces_left_up -= 1
        asterisk_up += 2
        spaces_right_up -= 1

    spaces_left_down = 1
    asterisk_down = (side_size * 2 - 3)
    spaces_right_down = 1
    while asterisk_down > 0:  # print the bottom triangle
        print((spaces_left_down * " ") + (asterisk_down * "*"))
        spaces_left_down += 1
        asterisk_down -= 2
        spaces_right_down += 1


# ************************ QUESTION 2 **************************
### WRITE CODE HERE
def lagrange_four_square_theorem(num):  # calc lagrange four square theorem to num
    found = []
    for i in range(0, int(num ** 0.5) + 1):  # run  until find 4 nums
        for j in range(0, int(num ** 0.5) + 1):
            for k in range(0, int(num ** 0.5) + 1):
                for p in range(0, int(num ** 0.5) + 1):
                    if i ** 2 + j ** 2 + k ** 2 + p ** 2 == num:
                        found.append([i, j, k, p])

    for B in found:  # sorting the four nums
        for K in range(len(B) - 1, 0, -1):
            for s in range(len(B) - 1, 0, -1):
                if B[s] < B[s - 1]:
                    B[s], B[s - 1] = B[s - 1], B[s]

    result = []  # save only one copy form the same 4 nums
    for i in found:
        if i not in result:
            result.append(i)

    return result


# ************************ QUESTION 3 **************************
### WRITE CODE HERE
def max_series(numbers):  # calc the len of the odd increase num is the list, and the bigger num % 3 = 0, in the list
    list_1 = []
    list_2 = []
    max_div_3 = -1
    for i in range(len(numbers)):
        if numbers[i] % 2 == 0:
            if len(list_2) > len(list_1):
                list_1 = list_2.copy()
            list_2 = []
        if numbers[i] % 2 != 0:  # calc the len of the odd increase num in the list
            if len(list_2) == 0:
                list_2.append(numbers[i])
            elif numbers[i] > numbers[i - 1]:
                list_2.append(numbers[i])
            elif numbers[i] < numbers[i - 1]:
                if len(list_2) > len(list_1):
                    list_1 = list_2.copy()
                list_2 = [numbers[i]]

        if numbers[i] % 3 == 0:  # calc the bigger num % 3 = 0, in the list
            if max_div_3 < numbers[i]:
                max_div_3 = numbers[i]

    if len(list_1) > len(list_2):
        return [len(list_1), max_div_3]
    return [len(list_2), max_div_3]

print(lagrange_four_square_theorem(0))