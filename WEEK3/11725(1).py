import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

parent = [0] * (N+1)

for i in range(N+1):
    parent[i] = i

edge = {i : [] for i in range(1, N+1)}

for _ in range(N-1):
    a, b = map(int, input().split())
    edge[a].append(b)
    edge[b].append(a) 

for i in range(N):
    edge[i+1].sort()

def bfs():
    queue = deque([1])
    while queue:
        k = queue.popleft()
        for child in edge[k]:
            if parent[child] == child:
                parent[child] = k
                queue.append(child)
                
bfs()
for i in range(2, N+1):
    print(parent[i])