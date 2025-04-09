import sys
from collections import deque

N = int(sys.stdin.readline())  # 맵 크기
K = int(sys.stdin.readline())  # 사과 개수

apple = set()
for i in range(K):
    x, y = map(int, sys.stdin.readline().split())
    apple.add((x, y))

L = int(sys.stdin.readline())
rotation = {}
for i in range(L):
    sec, rot = sys.stdin.readline().split()
    rotation[int(sec)] = rot

DIRECTION = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# 초기 설정
snake = deque([(1, 1)]) 
direction_idx = 0
time = 0



while True:

    time += 1

    head_x, head_y = snake[0]
    dx, dy = DIRECTION[direction_idx]
    new_head = (head_x + dx, head_y + dy)

    if not (1 <= new_head[0] <= N and 1 <= new_head[1] <= N):
        break

    if new_head in snake:
        break

    snake.appendleft(new_head)

    if new_head in apple:
        apple.remove(new_head)
    else:
        snake.pop()

    if time in rotation:
        if rotation[time] == "D":
            direction_idx = (direction_idx + 1) % 4
        elif rotation[time] == "L":
            direction_idx = (direction_idx - 1) % 4

print(time)