import sys
from collections import deque

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())

appleR = [0] * K
appleC = [0] * K

snake = deque()    # 뱀 x 위치

for i in range(K):
    appleC[i], appleR[i] = map(int, sys.stdin.readline().split())

L = int(sys.stdin.readline())
secondStr = [''] * L
secondInt = [0] * L
rotate = [''] * L

for i in range(L):
    secondStr[i], rotate[i] = map(str, sys.stdin.readline().split())

for i in range(L):
    secondInt[i]= int(secondStr[i])

# print()
# print(N) #맵 길이
# print(K)  #사과 개수
# print(appleC) # 사과 x
# print(appleR) # 사과 y
# print(L) # 방향 바꾸기 개수
# print(secondInt) #몇초 뒤
# print(rotate) #도는 방향

directionX = 0
directionY = 1
nowSecond = 0
nowSnake = (1,1)
snake.appendleft(nowSnake)
nowDirection = (directionX,directionY)

def snakeFunction(nowSnake, directionX,directionY, nowSecond):

    snake.appendleft(nowSnake)
    # 벽에 부딫히는거 확인
    # 머리랑 몸통,꼬리 겹치는지 확인하고
    # 사과 검사하고 
    snake.pop()

    for t in range(L):
        if nowSecond == secondInt[t]:
            if rotate[t] == 'D':
                directionX = directionY
                directionY = -directionX
            elif rotate[t] == 'L':
                directionX = -directionY
                directionY = directionX

    nextDirection = (directionX,directionY)

    nextSnake = tuple(sum(elem) for elem in zip(nowSnake,  nextDirection))

    return snakeFunction(nextSnake, directionX, directionY, nowSecond+1)