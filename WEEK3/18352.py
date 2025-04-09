import sys
from collections import deque

input = sys.stdin.readline

N, M, K, X = map(int, input().split())

town = {i: [] for i in range(N + 1)}
length = [-1] * (N + 1)
result = []

for _ in range(M):
    start, end = map(int, input().split())
    town[start].append(end)


def bfs(v):

    global length
    queue = deque([v])
    length[v] = 0
    while queue:
        k = queue.popleft()
        for i in town[k]:
            if length[i] == -1:
                queue.append(i)
                length[i] = length[k] + 1

bfs(X)

for i in range(len(length)):
    if length[i] == K:
        result.append(i)

if len(result) == 0:
    print(-1)
else:
    for j in result:
        print(j)
