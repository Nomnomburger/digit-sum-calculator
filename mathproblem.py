import math


def math_problem():
    x = input("Enter the number! ")
    digitSum = 0
    total = 0

    # print(math.trunc(remainder))

    for i in range(x + 1):

        remainder = math.fmod(i, 10)
        quotient = i / 10
        digitSum = 0

        while(quotient > 0):
            digitSum = digitSum + remainder
            remainder = math.fmod(quotient, 10)
            quotient = quotient / 10

        digitSum = digitSum + remainder

        total = total + digitSum

    print "The sum all digits from 1 to", x, "is:", math.trunc(total)
    raw_input()

math_problem()
