import sys
from collections import deque

input = sys.stdin.readline

M, N = map(int, input().split())
tomato = [[] for j in range(N)]
queue = deque()


for n in range(N):
    tomato[n] = list(map(int, input().split()))
    for m in range(M):
        if tomato[n][m] == 1:
            queue.append((n, m, 0))


direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def bfs():
    max_day = 0
    while queue:
        n, m, day = queue.popleft()
        max_day = max(max_day, day)

        for dn, dm in direction:
            nn, nm = n+dn, m+dm
            if 0<=nn<N and 0<=nm<M:
                if tomato[nn][nm] == 0:
                    tomato[nn][nm] = 1
                    queue.append((nn, nm, day+1))

    for n in range(N):
        for m in range(M):
            if tomato[n][m] == 0:
                return -1
                
    return max_day

print(bfs())