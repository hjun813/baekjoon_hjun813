import sys

input = sys.stdin.readline

N, M = map(int, input().split())

graph = {i: [] for i in range(1, N + 1)}
visited = [False] * (N + 1)
arr = []
count = 1

for _ in range(M):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

for key in graph:
    graph[key].sort()

print(graph)


def connected(v):
    visited[v] = True
    # 출력이나 리스트에 넣기
    arr.append(v)
    for i in graph[v]:
        if not visited[i]:
            connected(i)


connected(1)

if len(arr) != N:
    for i in range(1, N + 1):
        if not visited[i]:
            connected(i)
            count += 1

print(count)
