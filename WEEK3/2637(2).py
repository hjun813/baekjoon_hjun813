import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
M = int(input())

graph = {i: [] for i in range(1, N + 1)}
indegree = [0] * (N + 1)

for _ in range(M):
    X, Y, K = map(int, input().split())
    graph[Y].append((X, K))  # X를 만드는데 Y가 K개 필요함
    indegree[X] += 1

basic_parts = []
needed = [[0] * (N + 1) for _ in range(N + 1)]

queue = deque()
for i in range(1, N + 1):
    if indegree[i] == 0:
        queue.append(i)
        basic_parts.append(i)

while queue:

    part = queue.popleft()

    for next_part, count in graph[part]:
        if part in basic_parts:
            needed[next_part][part] += count
        else:
            for i in range(1, N + 1):
                needed[next_part][i] += needed[part][i] * count

        indegree[next_part] -= 1
        if indegree[next_part] == 0:
            queue.append(next_part)

for part in basic_parts:
    print(part, needed[N][part])
