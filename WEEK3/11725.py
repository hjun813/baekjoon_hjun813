import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
parent = [0] * (N + 1)

tree = {i: [] for i in range(1, N + 1)}

for _ in range(N - 1):
    node1, node2 = map(int, input().split())
    tree[node1].append(node2)
    tree[node2].append(node1)

for node in tree:
    tree[node].sort()

print(tree)

def bfs(v):
    queue = deque([v])
    while queue:
        node = queue.popleft()
        for child in tree[node]:
            if parent[child] == 0:
                parent[child] = node
                queue.append(child)

bfs(1)


for i in range(2, N + 1):
    print(parent[i])
