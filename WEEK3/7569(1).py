import sys
from collections import deque

input = sys.stdin.readline

M, N, H = map(int, input().split())

# 3차원 배열 입력받기
tomatoBox = []
queue = deque()

for h in range(H):
    floor = []
    for n in range(N):
        row = list(map(int, input().split()))
        for m in range(M):
            if row[m] == 1: # 1이면 걍 큐에다 다 넣어놓고 빼면서 바꿔주기
                queue.append((h, n, m, 0))  # (높이, 세로, 가로, 날짜)
        floor.append(row)
    tomatoBox.append(floor)

print(tomatoBox)

# 6방향 (위, 아래, 왼쪽, 오른쪽, 앞, 뒤)
directions = [(1,0,0), (-1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1)]

def bfs():
    max_day = 0  # 최종 익는 날짜
    while queue:
        h, n, m, day = queue.popleft()
        max_day = max(max_day, day)

        for dh, dn, dm in directions:
            nh, nn, nm = h + dh, n + dn, m + dm
            if 0 <= nh < H and 0 <= nn < N and 0 <= nm < M:
                if tomatoBox[nh][nn][nm] == 0:  # 안 익은 토마토만 처리
                    tomatoBox[nh][nn][nm] = 1  # 익힘 처리
                    queue.append((nh, nn, nm, day + 1))  # 날짜 증가하여 큐에 추가
    
    # 익지 않은 토마토가 남아 있는지 체크
    for h in range(H):
        for n in range(N):
            for m in range(M):
                if tomatoBox[h][n][m] == 0:
                    return -1  # 익지 않은 토마토가 남아있으면 -1 반환

    return max_day  # 모든 토마토가 익을 때까지 걸린 날짜 반환

print(bfs())
