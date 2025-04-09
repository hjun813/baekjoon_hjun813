import sys

input = sys.stdin.readline

n = int(input())
m = int(input())

graph = {i: [] for i in range(1, n + 1)}
visited = [False] * (n + 1)
downed = []

for _ in range(m):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

for node in graph:
    graph[node].sort()

# print(graph)


def virus(v):
    visited[v] = True
    downed.append(v)

    for i in graph[v]:
        if not visited[i]:
            virus(i)


virus(1)

print(len(downed) - 1)
