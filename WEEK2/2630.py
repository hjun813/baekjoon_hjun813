import sys

side = int(sys.stdin.readline())
paper = [0] * side
num = 0
blueCheck = 0
whiteCheck = 0

for i in range(side):
    paper[i] = list(map(int, sys.stdin.readline().split()))


def divide(n, a, b):  # a,b가 시작점, n 이 사이드 길이

    global blueCheck
    global whiteCheck

    color = paper[a][b] # 시작점 숫자 저장
    nextSide = int(n / 2)   # 다음 사이드 길이

    for i in range(a, a + n):
        for j in range(b, b + n):
            if paper[i][j] != color: # 모두 색이 같지 않으면 4개로 쪼개서 생각하기
                divide(nextSide, a, b)
                divide(nextSide, a, b + (nextSide))
                divide(nextSide, a + (nextSide), b)
                divide(nextSide, a + (nextSide), b + (nextSide))
                return# 함수 끝내야함 안끝내면 밑에꺼 계산함

    if color == 0:
        whiteCheck += 1
        
    else:
        blueCheck += 1


divide(side, 0, 0)
print(whiteCheck)
print(blueCheck)
