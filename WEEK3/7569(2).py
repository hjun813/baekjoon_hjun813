import sys
from collections import deque

input = sys.stdin.readline

M, N, H = map(int, input().split())
tomato = [[[] for j in range(N)] for i in range(H)]
queue = deque()

for h in range(H):
    for n in range(N):
        tomato[h][n] = list(map(int, input().split()))
        for m in range(M):
            if tomato[h][n][m] == 1:
                queue.append((h, n, m, 0))

print(tomato)
print(queue)

direction = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

def bfs():
    max_day = 0
    while queue:
        h, n, m, day = queue.popleft()
        max_day = max(max_day, day)

        for dh, dn, dm in direction:
            nh, nn, nm = h+dh, n+dn, m+dm
            if 0<=nh<H and 0<=nn<N and 0<=nm<M:
                if tomato[nh][nn][nm] == 0:
                    tomato[nh][nn][nm] = 1
                    queue.append((nh, nn, nm, day+1))

    for h in range(H):
        for n in range(N):
            for m in range(M):
                if tomato[h][n][m] == 0:
                    return -1
                
    return max_day

print(bfs())