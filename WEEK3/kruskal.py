import sys

v, e = map(int, input().split())
parent = [0] * (v+1)

for i in range(1, v+1):
    parent[i] = i

def find(parent, x): # 부모 찾기
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b): # 부모 합치기
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

edges = []
total = 0

for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))


edges.sort()
print(edges)

for i in range(e):
    cost, a, b = edges[i]
    if find(parent, a) != find(parent, b):  # 부모 다르면 연결
        union(parent, a, b) # 부모 합치기
        total += cost
print(total)