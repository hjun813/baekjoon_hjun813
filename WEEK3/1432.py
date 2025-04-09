import sys
from collections import deque
import heapq
input = sys.stdin.readline

N = int(input())

graph = []
edge = {i: [] for i in range(1, N + 1)}

for i in range(N):
    graph.append(list(map(str, input().strip())))

# print(graph)
indegree = [0] * (N+1)
outdegree= [0] * (N+1)

for i in range(N):
    for j in range(N):
        if graph[i][j] == "1":
            edge[i + 1].append(j + 1)
            indegree[j+1] += 1

for i in range(1,N+1):
    outdegree[i] = len(edge[i])

print(edge)
print(outdegree)
print(indegree)

queue = []
result = []

for i in range(1, N+1):
    if indegree[i] == 0:
        heapq.heappush(queue, i)

while queue:
    k = heapq.heappop(queue)
    
    result.append(k)
    for connect in edge[k]:
        indegree[connect] -= 1
        if indegree[connect] == 0:
            heapq.heappush(queue, connect)

# print(result)

# result 길이가 N과 같지 않으면 -1 
if len(result) != N:
    print(-1)
else:
    for i in range(1, N+1):
        for j in range(0,N):
            if result[j] == i:
                print(j+1, end=" ")

