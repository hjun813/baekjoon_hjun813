import sys
from collections import deque

input = sys.stdin.readline

R, C = map(int, input().split())
mapInfo = []
waterqueue = deque()
dochiqueue = deque()

direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
dochiVisit = [[-1 for _ in range(C)] for _ in range(R)]  # -1: 방문X, 0 이상: 이동 시간

for i in range(R):
    row = list(input().strip())
    mapInfo.append(row)
    for j in range(C):
        if row[j] == "D":
            homeSweetHome = (i, j)  # 비버 굴 위치
        elif row[j] == "S":
            dochiqueue.append((i, j))  # 고슴도치 큐에 추가
            dochiVisit[i][j] = 0  # 시작 지점 시간 0초
        elif row[j] == "*":
            waterqueue.append((i, j))  # 물 위치 모두 큐에 추가

def saveDochi():
    while dochiqueue:
        # print(mapInfo)
        # print()
        
        for _ in range(len(waterqueue)):
            wx, wy = waterqueue.popleft()
            for a, b in direction:
                nx, ny = wx + a, wy + b
                if 0 <= nx < R and 0 <= ny < C and mapInfo[nx][ny] == ".":
                    mapInfo[nx][ny] = "*"  # 물로 변경
                    waterqueue.append((nx, ny))

        
        for _ in range(len(dochiqueue)):
            dx, dy = dochiqueue.popleft()
            for a, b in direction:
                nx, ny = dx + a, dy + b
                if 0 <= nx < R and 0 <= ny < C:
                    if mapInfo[nx][ny] == "D":  # 비버 굴 도착 시 종료
                        print(dochiVisit[dx][dy] + 1)
                        return
                    if mapInfo[nx][ny] == "." and dochiVisit[nx][ny] == -1:
                        dochiVisit[nx][ny] = dochiVisit[dx][dy] + 1
                        dochiqueue.append((nx, ny))

    print("KAKTUS")  # 고슴도치가 도착할 수 없는 경우

saveDochi()
