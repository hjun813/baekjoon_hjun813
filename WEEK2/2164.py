import sys
from collections import deque

N = int(sys.stdin.readline())
a = []
for i in range(1, N + 1):
    a.append(i)
q = deque(a)

while N > 1:
    # print("cardlist", q)
    q.popleft()
    N = N - 1
    q.append(q[0])
    q.popleft()

print(q[0])