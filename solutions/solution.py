def solution(number):
    if number > 0:
        return sum([x for x in range(number) if x % 3 == 0 or x % 5 == 0])
    return 0


# Given a natural number,
# List all of the multiples of 3 or 5 below the natural number
# if the number is negative return -1
 # if the number is a multpile of both 3 and 5, only count once
 # Return the sum of the multiples
#
#
number = 10

print(solution(number))
