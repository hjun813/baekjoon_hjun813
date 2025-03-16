##다시 한번 짜볼것

def f(x, n):
    if x > 99 : 
        numList = list(map(str, str(x)))
        ans = numList[n]

        return int(ans)
    else : 
        return 1000


def hansu(x):
    count = 0

    if x < 100:
        count = x + 1
    elif x == 1000:
        count = 145
    else:
        count = 99
        for i in range(x):
            k = x - i
            if f(k, 0) - f(k, 1) == f(k, 1) - f(k, 2):
                count = count + 1
            else:
                continue
            
            if k < 100:
                break

    return count-1


num = int(input())

print(hansu(num))
