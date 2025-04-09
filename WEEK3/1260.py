import sys

input = sys.stdin.readline
from collections import deque

N, M, V = map(int, input().split())
dfsResult = []
bfsResult = []

graph = {i: [] for i in range(N + 1)}  # 딕셔너리로 저장

visitedDfs = [False] * (N + 1)
visitedBfs = [False] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()

# print(graph)


def dfs(graph, v, visitedDfs):  # v에서 dfs 하세요,
    visitedDfs[v] = True
    dfsResult.append(v)
    for i in graph[v]:
        if not visitedDfs[i]:
            dfs(graph, i, visitedDfs)


def bfs(graph, v, visitedBfs):  # v에서 bfs 하세요,
    queue = deque([v])
    visitedBfs[v] = True

    while queue:
        k = queue.popleft()
        bfsResult.append(k)
        for i in graph[k]:
            if not visitedBfs[i]:
                queue.append(i)
                visitedBfs[i] = True


dfs(graph, V, visitedDfs)
print(*dfsResult, end=" ")
print()
bfs(graph, V, visitedBfs)
print(*bfsResult, end=" ")
