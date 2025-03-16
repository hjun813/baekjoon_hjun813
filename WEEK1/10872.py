def factorial(x):
    if x == 1:
        return 1
    if x == 0:
        return 1
    else :
        answer = x * factorial(x-1)
        return answer

n = int(input())
ans = factorial(n)
print(ans)