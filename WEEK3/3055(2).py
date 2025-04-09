import sys
from collections import deque

input = sys.stdin.readline

R, C = map(int, input().split())
mapInfo = []
waterqueue = deque()
dochiqueue = deque()

direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
dochiVisit = [[-1 for _ in range(C)] for _ in range(R)]

for i in range(R):
    row = list(input().strip())
    mapInfo.append(row)
    for j in range(C):
        if row[j] == "D":
            homeSweetHome = (i, j)
        elif row[j] == "S":
            dochiqueue.append((i, j))
            dochiVisit[i][j] = 0
        elif row[j] == "*":
            waterqueue.append((i, j))

def saveDochi():
    while dochiqueue:
        for _ in range(len(waterqueue)):
            wx, wy = waterqueue.popleft()
            for a, b in direction:
                nx, ny = wx + a, wy + b
                if 0 <= nx < R and 0 <= ny < C and mapInfo[nx][ny] == ".":
                    mapInfo[nx][ny] = "*"
                    waterqueue.append((nx, ny))

        for _ in range(len(dochiqueue)):
            dx, dy = dochiqueue.popleft()
            for a, b in direction:
                nx, ny = dx + a, dy + b
                if 0 <= nx < R and 0 <= ny < C:
                    if mapInfo[nx][ny] == "D":
                        print(dochiVisit[dx][dy] + 1)
                        return
                    if mapInfo[nx][ny] == "." and dochiVisit[nx][ny] == -1:
                        dochiVisit[nx][ny] = dochiVisit[dx][dy] + 1
                        dochiqueue.append((nx, ny))

    print("KAKTUS")


saveDochi()
