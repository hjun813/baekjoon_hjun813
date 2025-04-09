# import sys
# from collections import deque

# N = int(sys.stdin.readline())
# K = int(sys.stdin.readline())

# appleR = [0] * K
# appleC = [0] * K

# snake = deque()    # 뱀 x 위치

# for i in range(K):
#     appleC[i], appleR[i] = map(int, sys.stdin.readline().split())

# L = int(sys.stdin.readline())
# secondStr = [''] * L
# secondInt = [0] * L
# rotate = [''] * L

# for i in range(L):
#     secondStr[i], rotate[i] = map(str, sys.stdin.readline().split())

# for i in range(L):
#     secondInt[i]= int(secondStr[i])

# # print()
# # print(N) #맵 길이
# # print(K)  #사과 개수
# # print(appleC) # 사과 x
# # print(appleR) # 사과 y
# # print(L) # 방향 바꾸기 개수
# # print(secondInt) #몇초 뒤
# # print(rotate) #도는 방향

# directionX = 0
# directionY = 1
# nowSecond = 0
# nowSnake = (1,1)
# snake.appendleft(nowSnake)
# nowDirection = (directionX,directionY)

# def snakeFunction(nowSnake, directionX,directionY, nowSecond):

#     snake.appendleft(nowSnake)
#     # 벽에 만나는거 확인
#     # 머리랑 몸통,꼬리 겹치는지 확인하고
#     # 사과 검사하고 
#     snake.pop()

#     for t in range(L):
#         if nowSecond == secondInt[t]:
#             if rotate[t] == 'D':
#                 directionX = directionY
#                 directionY = -directionX
#             elif rotate[t] == 'L':
#                 directionX = -directionY
#                 directionY = directionX

#     nextDirection = (directionX,directionY)

#     nextSnake = tuple(sum(elem) for elem in zip(nowSnake,  nextDirection))

#     return snakeFunction(nextSnake, directionX, directionY, nowSecond+1)

import sys
from collections import deque

# 입력 받기
N = int(sys.stdin.readline())  # 맵 크기
K = int(sys.stdin.readline())  # 사과 개수

# 사과 위치 저장 (set 사용 -> O(1) 탐색)
apples = set()
for _ in range(K):
    x, y = map(int, sys.stdin.readline().split())
    apples.add((x, y))

L = int(sys.stdin.readline())  # 방향 변환 횟수
rotations = {}  # {시간: 방향} 딕셔너리
for _ in range(L):
    sec, rot = sys.stdin.readline().split()
    rotations[int(sec)] = rot

# 방향 (우, 하, 좌, 상) -> 시계방향 기준
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# 초기 설정
snake = deque([(1, 1)])  # 뱀 위치 (머리가 첫 번째 원소)
direction_idx = 0  # 초기 방향 (오른쪽)
time = 0  # 시간


# 게임 실행
while True:
    time += 1
    
    # 현재 방향으로 머리 이동
    head_x, head_y = snake[0]
    dx, dy = DIRECTIONS[direction_idx]
    new_head = (head_x + dx, head_y + dy)
    
    # 벽 충돌 체크
    if not (1 <= new_head[0] <= N and 1 <= new_head[1] <= N):
        break
    
    # 자기 몸과 충돌 체크
    if new_head in snake:
        break
    
    # 이동
    snake.appendleft(new_head)
    
    # 사과 여부 확인
    if new_head in apples:
        apples.remove(new_head)  # 사과 먹음 (길이 유지)
    else:
        snake.pop()  # 사과 없으면 꼬리 제거 (길이 유지)
    
    # 방향 전환 체크
    if time in rotations:
        if rotations[time] == 'D':  # 오른쪽 회전 (시계 방향)
            direction_idx = (direction_idx + 1) % 4
        elif rotations[time] == 'L':  # 왼쪽 회전 (반시계 방향)
            direction_idx = (direction_idx - 1) % 4

# 게임 종료 후 걸린 시간 출력
print(time)
# 다시한번 