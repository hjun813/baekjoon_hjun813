import sys
from collections import deque

K = int(sys.stdin.readline())
record = []
a = [] 
q = deque(a)

for i in range(K):
    record.append(int(sys.stdin.readline()))

for i in range(K):
    if record[i] == 0:
        q.pop()
    else:
        q.append(record[i])

print(sum(q))