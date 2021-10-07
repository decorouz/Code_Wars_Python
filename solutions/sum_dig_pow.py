import math


def sum_dig_pow(a, b):  # range(a, b + 1) will be studied by the function
    lst = []
    for num in range(a, b+1):
        if num > 9:
            s = sum_dig(num)
            if s == num:
                lst.append(num)
        else:
            lst.append(num)
    return lst


def sum_dig(num):
    pw = 1
    total = 0
    for dig in str(num):
        total += int(dig)**pw
        pw += 1
    return total


print(sum_dig_pow(1, 100))
