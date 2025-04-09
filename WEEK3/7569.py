import sys
from collections import deque
input = sys.stdin.readline

M, N, H = map(int, input().split())

tomatoBox = [[[] for j in range(N)] for i in range(H)]
queue = deque()

for h in range(H):
    for n in range(N):
        tomatoBox[h][n] = (list(map(int, input().split())))
        for m in range(M):
            if tomatoBox[h][n][m] == 1: # 1이면 걍 큐에다 다 넣어놓고 빼면서 바꿔주기
                queue.append((h, n, m, 0)) # 좌표 + day
        

direction = [(1,0,0), (-1,0,0), (0,1,0), (0,-1,0),(0,0,1), (0,0,-1)]
# print(tomatoBox)
def bfs():
    max_day = 0
    while queue:
        h, n, m, day = queue.popleft()
        max_day = max(day, max_day)

        for dh, dn, dm in direction:
            nh, nn, nm  = h+dh, n+dn, m+dm
            if 0<= nh<H and 0<=nn<N and 0<= nm<M:
                if tomatoBox[nh][nn][nm] ==0:
                    tomatoBox[nh][nn][nm] = 1
                    queue.append((nh, nn, nm, day+1))
                    
    for h in range(H):
        for n in range(N):
            for m in range(M):
                if tomatoBox[h][n][m] == 0:
                    return -1
                
    return max_day

print(bfs())
