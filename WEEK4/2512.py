import sys
input = sys.stdin.readline

N = int(input())
local = list(map(int, input().split()))
M = int(input())

low = 0
high = max(local)
answer = 0

while True:
    if low < high:
        mid = int((low + high)/2)
        total = 0
        for money in local:
            if money < mid:
                total += money
            else:
                total += mid
        if total == M:
            answer = mid
            break
        elif total < M:
            low = mid +1
        else:
            high = mid -1
    else:
        check = 0
        for money in local:
            if money < low:
                check += money
            else:
                check += low
        if check > M:
            answer = low -1
        else:
            answer = low
        break

print(answer)