import math

testcaseNum = int(input())


def primeNum(x, n):

    if x == 2:
        return True
    
    for i in range(2, n + 1):
        if x % i == 0:

            return False

    return True


for i in range(testcaseNum):

    testcase = int(input())
    half = int(testcase / 2)
    sqrtHalf = int(math.sqrt(half))

    left = half
    right = testcase - left

    for j in range(0, 5000):

        if primeNum(left, sqrtHalf) & primeNum(right, sqrtHalf+1):

            print(left,right)
            break
        else:

            left = left - 1
            right = right + 1

