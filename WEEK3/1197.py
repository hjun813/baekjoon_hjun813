import sys
sys.setrecursionlimit(10**4)
V, E = map(int, sys.stdin.readline().split())

edge = []


for i in range(E):
    node, node2, weight = map(int, sys.stdin.readline().split())
    edge.append((weight, node, node2))


edge.sort()
parent = [0] * (V + 1)
total = 0


for i in range(1, V+1):
    parent[i] = i


def find(parent, v):
    if parent[v] != v:
        parent[v] = find(parent, parent[v])
    return parent[v]


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for i in range(E):
    cost, a, b = edge[i]

    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        total += cost

print(total)