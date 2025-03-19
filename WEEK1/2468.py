import sys
sys.setrecursionlimit(10**6)
num = int(input())

rows = num
cols = num
island = [[0 for j in range(cols)] for i in range(rows)]  # 높이 정보 가져오기
islandDrowned = [
    [False for j in range(cols + 2)] for i in range(rows + 2)
]  # 잠겼는지 아닌지, index에 상하좌우 1씩 추가함
count = 0
Checking = [[False for j in range(cols + 2)] for i in range(rows + 2)]  # # 섬 체크 여부

numberIsland = []


for i in range(num + 2):
    islandDrowned[0][i] = True
for i in range(num + 2):
    islandDrowned[num + 1][i] = True
for i in range(num):
    islandDrowned[i + 1][0] = True
    islandDrowned[i + 1][num + 1] = True

for i in range(num + 2):
    Checking[0][i] = True
for i in range(num + 2):
    Checking[num + 1][i] = True
for i in range(num):
    Checking[i + 1][0] = True
    Checking[i + 1][num + 1] = True


R = 0  # 최대 비 양 저장
Rr = 0
maxR = [0] * num  # 최대 비 얼마나 올지
minR = [0] * num  # 최대 비 얼마나 올지
safeSpace = 0  # 안전 지역 수

for i in range(num):
    island[i] = list(map(int, sys.stdin.readline().rstrip().split()))


def maxRain(arr):  # 최대 비 얼마나 올지 최대 비 양 리턴

    for i in range(num):
        maxR[i] = max(arr[i])

    return max(maxR)


def minRain(arr):  # 최소 비 얼마나 올지 최대 비 양 리턴

    for i in range(num):
        maxR[i] = min(arr[i])

    return min(maxR)


def rainyDay(n, safeSpace, count):  # n은 비온양

    if n == R :
        numberIsland.append(1)
    elif n != R - 1:  # 최대 잠길때까지 재귀 돌려요
        for i in range(num):
            for j in range(num):
                island[i][j] -= 1
                if island[i][j] == 0:
                    islandDrowned[i + 1][j + 1] = True

        checkDrowned(islandDrowned, count)

        for i in range(num + 2):
            for j in range(num + 2):
                Checking[i][j] = False
        for i in range(num + 2):
            Checking[0][i] = True
        for i in range(num + 2):
            Checking[num + 1][i] = True
        for i in range(num):
            Checking[i + 1][0] = True
            Checking[i + 1][num + 1] = True

        rainyDay(n + 1, safeSpace, 0)
    



def checkDrowned(arr, count):  # islandDrowned를 받을 거임

    for i in range(1, num + 1):
        for j in range(1, num + 1):

            if not Checking[i][j]:
                if not islandDrowned[i][j]:
                    count = count + 1

            islandcheck(i, j, count, Checking)

    numberIsland.append(count)


def islandcheck(i, j, n, Checking):
    global count

    if not Checking[i][j]:
        Checking[i][j] = True
        if not islandDrowned[i][j]:
            Checking[i][j] = True

            if not Checking[i][j + 1]:
                if not islandDrowned[i][j + 1]:  # 우
                    islandcheck(i, j + 1, n, Checking)
            if not Checking[i + 1][j]:
                if not islandDrowned[i + 1][j]:  # 하
                    islandcheck(i + 1, j, n, Checking)
            if not Checking[i][j - 1]:  # 좌
                if not islandDrowned[i][j - 1]:
                    islandcheck(i, j - 1, n, Checking)
            if not Checking[i - 1][j]:
                if not islandDrowned[i - 1][j]:  # 상
                    islandcheck(i - 1, j, n, Checking)


R = maxRain(island)
Rr = minRain(island)
if R == Rr:
    rainyDay(R, 0, 0)
else:
    rainyDay(Rr-1, 0, 0)

if len(numberIsland) == 0:
    print(1)
else:
    print(max(numberIsland))
