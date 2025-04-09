import sys
from collections import deque
import heapq

input = sys.stdin.readline

R, C = map(int, input().split())
mapInfo = []
Rock = []
direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
dochiVisit = [[False for i in range(C)] for j in range(R)]

for i in range(R):
    mapInfo.append(list(map(str, input().strip())))

print(mapInfo)

for i in range(R):
    for j in range(C):
        if mapInfo[i][j] == "D":
            homeSweetHome = [i, j]
        elif mapInfo[i][j] == "S":
            dochi = [i, j]
        elif mapInfo[i][j] == "*":
            water = [i, j]
        elif mapInfo[i][j] == "X":
            Rock.append([i, j])

start_x, start_y = dochi
dochiVisit[start_x][start_y] = True


def saveDochi():
    dochiqueue = deque(dochi)
    waterqueue = deque(water)

    # 물 먼저 넘치고
    # 고슴 도치가 남은 곳 중 이동
    while dochiqueue:

        for _ in range(len(waterqueue)):
            wx, wy = waterqueue.popleft()
            for a, b in direction:
                if 0 <= wx + a < C and 0 <= wy + b < R:
                    if mapInfo[wx + a][wy + b] == ".":
                        mapInfo[wx + a][wy + b] = "*"
                        waterqueue.append([wx + a, wy + b])
                    elif mapInfo[wx + a][wy + b] == "S":
                        mapInfo[wx + a][wy + b] = "*"
                        waterqueue.append([wx + a, wy + b])

        dx, dy = dochiqueue.popleft()

        for a, b in direction:
            if 0 <= dx + a < C and 0 <= dy + b < R:
                if not dochiVisit[dx + a][dy + b]:
                    if mapInfo[dx + a][dy + b] == ".":
                        dochiqueue.append([dx + a, dy + b])
        
  
