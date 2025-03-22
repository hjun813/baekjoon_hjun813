##########################################다시 짜보기######################################
import sys

N = int(sys.stdin.readline())

liquidInfo = list(map(int, sys.stdin.readline().split()))

liquidInfo.sort()

left = 0
right = N - 1
need = []
firstL = liquidInfo[0]
secondL = liquidInfo[-1]
beforeSum = firstL + secondL

while left < right:

    sumLiquid = liquidInfo[left] + liquidInfo[right]

    if sumLiquid == 0:
        firstL = liquidInfo[left]
        secondL = liquidInfo[right]
        break

    if abs(sumLiquid) < abs(beforeSum):
        firstL = liquidInfo[left]
        secondL = liquidInfo[right]
        beforeSum = sumLiquid

    if sumLiquid > 0:
        right = right - 1

    elif sumLiquid < 0:
        left = left + 1

    

need.append(firstL)
need.append(secondL)
need.sort()

print(need[0], need[1])