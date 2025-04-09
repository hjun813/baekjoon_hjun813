import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
edge = []

for _ in range(M):
    start, end = map(int, input().split())
    edge.append((start, end))

# print(edge)


def standingLine():

    graph = {i: [] for i in range(1, N + 1)}
    indegree = {i: 0 for i in range(1, N + 1)}

    for start, end in edge:
        graph[start].append(end)
        graph[start].sort()
        indegree[end] += 1

    queue = deque([node for node in indegree if indegree[node] == 0])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)

        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    return result


print(*standingLine())