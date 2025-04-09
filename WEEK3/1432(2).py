import sys
from collections import deque
import heapq
input = sys.stdin.readline

N = int(input())

graph = []
edge = {i: [] for i in range(1, N + 1)}

for i in range(N):
    graph.append(list(map(str, input().strip())))

outdegree= [0] * (N+1)

for i in range(N):
    for j in range(N):
        if graph[i][j] == "1":
            edge[i + 1].append(j + 1)

for i in range(1,N+1):
    outdegree[i] = len(edge[i])

queue = []
result = [0] * (N+1)
renum = N
for i in range(1, N+1):
    if outdegree[i] == 0:
        heapq.heappush(queue, -i)

while queue:

    k = heapq.heappop(queue)
    result[-k] = renum
    renum -= 1
    for i in range(1, N+1):
        if -k in edge[i]:
            outdegree[i] -= 1
            if outdegree[i] == 0:
                heapq.heappush(queue, -i)


if 0 in result[1:N+1]:
    print(-1)
else:
    print(*result[1:N+1], end=" ")

