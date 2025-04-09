import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

numberInt = [0] * N
number = list(map(str, sys.stdin.readline()))
number.pop()
dq = deque()
print(number)

for i in range(N):
    numberInt[i] = int(number[i])

print(numberInt)

for numberInt in numberInt:
    print(numberInt)
    if len(dq) == 0:
        dq.append(numberInt)
    else:
        if K > 0:
            if dq[-1] < numberInt:
                while len(dq) > 0 and dq[-1] < numberInt and K > 0:
                    dq.pop()
                    K -= 1
                dq.append(numberInt)
            elif dq[-1] >= numberInt:
                dq.append(numberInt)

        else:
            dq.append(numberInt)
    print(dq)
    print()

print(K)
for i in dq:
    print(i, end='')
print()
if K != 0:
    for _ in range(K):
        delete = min(dq)
        dq.remove(delete)
        

for i in dq:
    print(i, end="")
