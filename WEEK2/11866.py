#======================= 요세 푸스 ===============================
import sys
from collections import deque
N, K = map(int, sys.stdin.readline().split())
people = []
qpeople = deque(people)
result = []

for i in range(1, N+1):
    qpeople.append(i)

while len(qpeople)>1:

    for i in range(K-1):
        pop = qpeople.popleft()
        qpeople.append(pop)

    delete = qpeople.popleft()
    result.append(delete)

result.append(qpeople[0])

print("<", end='')
for i in range(len(result) -1):
    print(result[i], end=", ")
print(result[-1], end="")
print(">", end='')